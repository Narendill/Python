# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов
from typing import Callable
from random import randint

__all__ = ['check_params', 'quiz']


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


@check_params
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
    quiz(10, 30)
