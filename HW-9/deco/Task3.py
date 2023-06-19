# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json
from typing import Callable
from pathlib import Path

__all__ = ['save_params']


def save_params(func: Callable):
    to_append = {}  # Храним то, что записываем в json
    iteration = 0  # Выступает как ключ для сохранения результата и *args

    def wrapper(*args, **kwargs):
        nonlocal to_append
        nonlocal iteration

        # Проверяем есть ли файл и не пустой ли он
        if Path(f'{func.__name__}.json').exists() and Path(f'{func.__name__}.json').stat().st_size > 0:
            with open(f'{func.__name__}.json', 'r', encoding='utf-8') as f_json:
                to_append = json.load(f_json)
                # Для итераций ищем последнюю максимальную
                for key in to_append.keys():
                    if key.isdigit() and int(key) > iteration:
                        iteration = int(key)

        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f_json:
            result = func(*args, **kwargs)
            to_append.setdefault(iteration + 1, tuple([*args, result]))
            to_append.update(**kwargs)
            json.dump(to_append, f_json, ensure_ascii=False, indent=2)
            print(f'\033[36mFile {func.__name__}.json was updated.\033[0m')
        iteration += 1
        return result
        iteration = 0

    return wrapper


@save_params
def _summ(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    print(_summ(55, 150, s=10))
    print(_summ(155, 150, q=10))
    print(_summ(t=5, q=10))
