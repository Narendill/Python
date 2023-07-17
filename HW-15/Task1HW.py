# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# ________________________________________________________
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

import logging
import argparse


def type_triangle(a: int | float, b: int | float, c: int | float) -> str:
    if a + b > c and a + c > b and c + b > a:
        if a == b == c:
            message = '\033[94mРавносторонний треугольник.\033[0m'
        elif a == b or a == c or b == c:
            message = '\033[94mРавнобедренный треугольник.\033[0m'
        else:
            message = '\033[94mРазносторонний треугольник.\033[0m'
        logger.info(f'{message[5:-5]}: {a} - {b} - {c}')
        return message
    else:
        message = '\033[94mТреугольник не существует.\033[0m'
        logger.info(f'{message[5:-5]}: {a} - {b} - {c}')
        return message


if __name__ == '__main__':
    logging.basicConfig(filename='Task1HW.log', level=logging.NOTSET, encoding='utf-8',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='Парсер содержимого папки.')
    parser.add_argument('a', metavar='a', type=float, help='Введите длину первой стороны.')
    parser.add_argument('b', metavar='b', type=float, help='Введите длину второй стороны.')
    parser.add_argument('c', metavar='c', type=float, help='Введите длину третьей стороны.')
    args = parser.parse_args()

    print(type_triangle(args.a, args.b, args.c))
