# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые, т.е не мая, а 5.

import datetime
import calendar
import logging
import argparse


def get_date(user_date: str):

    months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
               7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
    weekdays = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг',
                4: 'пятница', 5: 'суббота', 6: 'воскресенье'}

    date_list = user_date.lower().split()

    # Парсим позиции
    try:
        week_number, week_day, month = int(date_list[0].split('-')[0]), date_list[1], date_list[2]
    except Exception as e:
        print(e)
        logger.error(f'{e} - неверный формат ввода данных - \'{user_date}\'.')
        raise ValueError(f'Неверный формат ввода данных: {e}.')

    # Парсим месяц
    for key, value in months.items():
        if value == month:
            month = key
    if month not in months.keys():
        logger.error(f'введен странный месяц \'{user_date}\'.')
        raise Exception('Введен странный месяц.')

    # Парсим день недели
    for key, value in weekdays.items():
        if value == week_day:
            week_day = key
    if week_day is None:
        logger.error(f'введен странный день недели \'{user_date}\'.')
        raise Exception('Введен странный день недели.')

    # Парсим полную дату
    count = 0
    for i in range(1, calendar.monthrange(datetime.datetime.now().year, 11)[1] + 1):
        date = datetime.datetime(datetime.datetime.now().year, month, i)
        if date.weekday() == week_day:
            count += 1
            if count == week_number:
                return date.date()
    logger.error(f'такого дня не существует - \'{user_date}\'.')
    raise Exception('Такого дня не существует.')


if __name__ == '__main__':
    logging.basicConfig(filename='info.log', level=logging.NOTSET, encoding='utf-8',
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)
    parser = argparse.ArgumentParser(description='Парсер аргументов для функции get_date.')
    parser.add_argument('-user_date', metavar='user_date', type=str,
                        help='Введи строку в формате: "1-й четверг сентября".', default=None)

    parser.add_argument('-which', metavar='which', type=int,
                        help='Введи порядковый номер дня недели.', default=1)
    parser.add_argument('-week_day', metavar='week_day', type=str,
                        help='Введи день недели или его номер.', default=str(datetime.datetime.now().weekday()))
    parser.add_argument('-month', metavar='month', type=str,
                        help='Введи месяц или его номер.', default=str(datetime.datetime.now().month))

    args = parser.parse_args()

    if args.user_date is not None:
        print(get_date(args.user_date))
    else:
        months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
                  7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
        weekdays = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг',
                    4: 'пятница', 5: 'суббота', 6: 'воскресенье'}

        all_args = f'{args.which}-й'

        if args.week_day.isdigit():
            for digit in weekdays.keys():
                if args.week_day == str(digit):
                    all_args += f' {weekdays[digit]}'
        else:
            all_args += f' {args.week_day.lower()}'

        if args.month.isdigit():
            for digit in months.keys():
                if args.month == str(digit):
                    all_args += f' {months[digit]}'
        else:
            months = {'январь': 'января', 'февраль': 'февраля', 'март': 'марта', 'апрель': 'апреля', 'май': 'мая',
                      'июнь': 'июня', 'июль': 'июля', 'август': 'августа', 'сентябрь': 'сентября', 'октябрь': 'октября',
                      'ноябрь': 'ноября', 'декабрь': 'декабря'}
            for key, value in months.items():
                if key == args.month.lower():
                    all_args += f' {value}'

        print(get_date(all_args))

        # Примеры ввода в консоль:

        # python Task5.py -user_date "1-й понедельник июля"
        # python Task5.py -which 1 -week_day 1 -month 7
        # python Task5.py -week_day 1 -month 7
        # python Task5.py
        # python Task5.py -which 1 -week_day понедельник -month 7
        # python Task5.py -which 1 -week_day 0 -month 7
