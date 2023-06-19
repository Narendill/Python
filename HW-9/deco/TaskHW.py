# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
import csv
import json
from typing import Callable
from random import randint

__all__ = ['equation_solution', 'gen_csv']


def gen_csv() -> None:
    """Функция для генерации csv-файла под именем 'gen_csv.csv'."""
    MIN_NUMBER = -1000
    MAX_NUMBER = 1000
    MIN_ROWS = 100
    MAX_ROWS = 1000
    with open('gen_csv.csv', 'w', encoding='utf-8', newline='') as f_write:
        rows = randint(MIN_ROWS, MAX_ROWS)
        csv_writer = csv.writer(f_write)
        for _ in range(rows):
            csv_writer.writerow(
                [randint(MIN_NUMBER, MAX_NUMBER),
                 randint(MIN_NUMBER, MAX_NUMBER),
                 randint(MIN_NUMBER, MAX_NUMBER)])
        print(f'\033[36mFile \'gen_csv.csv\' was created with {rows} lines.\033[0m')


def start_solution(func: Callable):
    """Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла."""
    result = {}

    def wrapper(*args, **kwargs):
        # Открыли csv, прочитали в список whole_file
        with open('gen_csv.csv', 'r', encoding='utf-8', newline='') as f_read:
            csv_reader = csv.reader(f_read)
            whole_file = [line for line in csv_reader]

        for line in whole_file:
            to_add = {str(tuple([int(num) for num in line])): func(*[int(num) for num in line])}
            result.update(to_add)

        return result

    return wrapper


def write_results(func: Callable):
    """Декоратор, сохраняющий переданные параметры и результаты работы функции в json-файл."""
    result = {}

    def wrapper(*args, **kwargs):
        with open('gen_json.json', 'w', encoding='utf-8') as f_write:
            to_add = func(*args)
            result.update(to_add)
            json.dump(to_add, f_write, ensure_ascii=False, indent=4)
            print(f'\033[36mFile \'gen_json.json\' was created.\033[0m')
            return result

    return wrapper


@write_results
@start_solution
def equation_solution(a: int, b: int, c: int) -> list[int | complex]:
    """Функция для нахождения корней квадратного уравнения."""
    # Добавил проверку на значение а, т.к. при генерации оно может быть равно нулю, а тогда это уже не будет квадратное
    # уравнение. Можно было бы сделать проверку при генерации, но какая разница? :)
    if a == 0:
        return 'a не может быть равно нулю'

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = round((-b + discriminant ** 0.5) / 2 / a, 2)
        x2 = round((-b - discriminant ** 0.5) / 2 / a, 2)
        return [x1, x2]
    elif discriminant == 0:
        x1 = round(-b / 2 / a, 2)
        return [x1]
    else:
        x1 = (-b + complex(discriminant ** 0.5)) / 2 / a
        x2 = (-b - complex(discriminant ** 0.5)) / 2 / a
        x1 = round(x1.real, 2) + round(x1.imag, 2) * 1j
        x2 = round(x2.real, 2) + round(x2.imag, 2) * 1j
        return [str(x1), str(x2)]  # преобразовал в str, т.к. в json не работает complex


if __name__ == '__main__':
    gen_csv()
    equation_solution()
