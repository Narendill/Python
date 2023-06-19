# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 
from typing import Callable

__all__ = ['quiz']


def quiz(number: int, tries: int) -> Callable[[], None]:
    def get_number():
        for i in range(tries):
            guess_number = int(input('Какое число загадано? '))
            if guess_number == number:
                print(f'Ты угадал с {i + 1} попытки!')
                break
        else:
            print('Ты не угадал!')
            print('Конец игры...')

    return get_number


if __name__ == '__main__':
    quiz(10, 3)()
