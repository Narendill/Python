# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
import json
from typing import Callable
from random import randint
from pathlib import Path

__all__ = ['check_params', 'save_params', 'how_many_times', 'quiz']


def check_params(func: Callable):
    MAX_NUMBER = 100
    MAX_TRIES = 10
    MINIMUN = 1

    def wrapper(*args):
        number, tries = args[0], args[1]
        if number < MINIMUN or number > MAX_NUMBER:
            print(f'Загаданное число вне диапазона [{MINIMUN}, {MAX_NUMBER}], загадываю новое...')
            number = randint(MINIMUN, MAX_NUMBER)
        if tries < MINIMUN or tries > MAX_TRIES:
            print(f'Попытки вне диапазона [{MINIMUN}, {MAX_TRIES}], загадываю новое число попыток...')
            tries = randint(MINIMUN, MAX_TRIES)
        return func(number, tries)

    return wrapper


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


def how_many_times(num: int = 1):
    def deco(func: Callable):
        result = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return deco


@check_params
@how_many_times(3)
@save_params
def quiz(number, tries):
    for i in range(tries):
        guess_number = int(input('Какое число загадано? '))
        if guess_number == number:
            print(f'Ты угадал с {i + 1} попытки!')
            break
        else:
            print('Ты не угадал!')
            if i == tries - 1:
                print('Конец игры...')


if __name__ == '__main__':
    print(quiz.__name__)
    quiz(-5, 1)
