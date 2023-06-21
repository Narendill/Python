# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата

class Hexadecimal:

    def __init__(self, number_dec: int):
        self.number_dec = number_dec
        self.number_hex = self.__to_hex()

    def __to_hex(self) -> str:
        number_10 = self.number_dec
        number_16 = ''
        while number_10 > 0:
            match str(number_10 % 16):
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
                    number_16 = str(number_10 % 16) + number_16
            number_10 = number_10 // 16

        return number_16

    def __str__(self):
        return f'({self.number_dec}, {self.number_hex})'


if __name__ == '__main__':
    num = Hexadecimal(999)
    print(num)
