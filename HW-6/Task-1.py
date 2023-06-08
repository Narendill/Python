# В модуль с проверкой даты добавьте возможность
# запуска в терминале с передачей даты на проверку.

from sys import argv


def does_data_exist(data: str) -> bool:
    data = [int(i) for i in data.split('.')]
    
    if 1 <= data[2] <= 9999: # Проверяем год
        if 1 <= data[1] <= 12: # Проверяем месяц
            if 1 <= data[0] <= 31 and data[1] in [1, 3, 5, 7, 8, 10, 12]: # Проверяем дни по месяцам
                return True
            elif 1 <= data[0] <= 30 and data[1] in [4, 6, 9, 11]:
                return True
            elif (_get_leap_year(data[2]) and 1 <= data[0] <= 29) or (not _get_leap_year(data[2]) and 1 <= data[0] <= 28):
                return True
            else:
                return False
    return False


def _get_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(does_data_exist(argv[1]))