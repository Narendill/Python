# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата


def to_16(number: int) -> str:
    
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
    
    return number_16
    
    

number = int(input('Введи целое число: '))
print(f'{number} = {to_16(number)}')

# Проверка
print('________________________')
print(f'{number} = {hex(number)}')


