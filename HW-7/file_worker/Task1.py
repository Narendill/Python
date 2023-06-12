# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции

__all__ = ['write_numbers']
_MIN_NUMBER = -1000
_MAX_NUMBER = 1000


def write_numbers(name: str, rows: int) -> None:
    """Функция создает файл numbers.txt и заполняет его случайными парами чисел, разделенных знаком '|'."""
    from random import randint, uniform # Внезапно нашел тут: https://stackoverflow.com/questions/45331744/hide-import-in-library-python
    
    
    with open(name, 'a', encoding='utf-8') as f:
        for i in range(rows):
            print(f'{randint(_MIN_NUMBER, _MAX_NUMBER)}|{uniform(_MIN_NUMBER, _MAX_NUMBER)}', file=f)


if __name__ == '__main__':
    write_numbers('numbers.txt', 10)
