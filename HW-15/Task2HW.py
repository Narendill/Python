# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# ________________________________________________________
# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

import argparse
import logging


def to_16(number: int) -> str:
    number_to_log = number
    number_16 = ''
    while number > 0:
        match str(number % 16):
            case '10':
                number_16 = 'A' + number_16
            case '11':
                number_16 = 'B' + number_16
            case '12':
                number_16 = 'C' + number_16
            case '13':
                number_16 = 'D' + number_16
            case '14':
                number_16 = 'E' + number_16
            case '15':
                number_16 = 'F' + number_16
            case _:
                number_16 = str(number % 16) + number_16
        number = number // 16

    logger.info(f'{number_to_log} - {number_16}')
    return number_16


if __name__ == '__main__':
    logging.basicConfig(filename='Task2HW.log', level=logging.NOTSET, encoding='utf-8',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='Парсер аргумента для перевода целого числа в 16-ную систему.')
    parser.add_argument('number', metavar='number', type=int, help='Введите число для перевода.')
    args = parser.parse_args()

    print(to_16(args.number))
