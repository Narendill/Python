# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

from random import randint, uniform, choice
from pathlib import Path


class PathWork:
    def __init__(self, path: str | Path):
        self.path = path

    def generate_numbers(self, rows: int):
        """"Метод заполняет файл случайными парами чисел
        rows - количество строк"""
        path = Path(self.path) / 'PathWork_generate_numbers.txt'
        MIN_NUMBER = -1000
        MAX_NUMBER = 1000

        with open(Path(path), 'w', encoding='utf-8') as f:
            for i in range(rows):
                print(f'{randint(MIN_NUMBER, MAX_NUMBER)}|{uniform(MIN_NUMBER, MAX_NUMBER)}', file=f)
        print('\033[96mFile \'PathWork_write_numbers_to_file.txt\' was created.\033[0m')

    def generate_username(self, how_many_names: int):
        """Метод генерирует файл с пседвоименами"""
        path = Path(self.path) / 'PathWork_generate_username.txt'
        MIN_LETTERS = 4
        MAX_LETTERS = 7
        vowles = 'ёуеыаоэяию'
        cons = 'йцкнгшщзхфвпрлджчсмтб'

        result = ''
        list_result = []
        choose = randint(0, 1)

        for _ in range(how_many_names):
            for i in range(randint(MIN_LETTERS, MAX_LETTERS)):
                if choose == 0:
                    result += choice(vowles)
                    choose = 1
                else:
                    result += choice(cons)
                    choose = 0
            list_result.append(result)
            result = ''

        with open(path, 'w', encoding='utf-8') as f:
            for name in list_result:
                print(name[0].upper() + name[1:], file=f)
        print('\033[96mFile \'PathWork_generate_username.txt\' was created.\033[0m')

    def join_numbers_usernames(self):
        """Метод создает новый файл на основании файла с именами и файла с числами, если таковые присутствуют."""
        path = Path(self.path) / 'PathWork_join_numbers_usernames.txt'
        numbers_file = Path(self.path) / 'PathWork_generate_numbers.txt'
        usernames_file = Path(self.path) / 'PathWork_generate_username.txt'

        if numbers_file.exists() and usernames_file.exists():
            with (
                open(numbers_file, 'r', encoding='utf-8') as f1,
                open(usernames_file, 'r', encoding='utf-8') as f2,
                open(path, 'w', encoding='utf-8') as f3
            ):
                f1, f2 = list(f1), list(f2)
                index_f1 = 0
                index_f2 = 0

                if len(f1) >= len(f2):
                    for i in range(len(f1)):
                        if index_f2 >= len(f2):
                            index_f2 = 0
                        a, b = f1[i].replace('\n', '').split('|')

                        if float(a) * float(b) < 0:
                            print(f2[index_f2][:-1].lower(), abs(float(a) * float(b)), file=f3)
                        else:
                            print(f2[index_f2][:-1].upper(), round(float(a) * float(b)), file=f3)
                        index_f2 += 1
                else:
                    for i in range(len(f2)):
                        if index_f1 >= len(f1):
                            index_f1 = 0
                        a, b = f1[index_f1].replace('\n', '').split('|')

                        if float(a) * float(b) < 0:
                            print(f2[i][:-1].lower(), abs(float(a) * float(b)), file=f3)
                        else:
                            print(f2[i][:-1].upper(), round(float(a) * float(b)), file=f3)
                        index_f1 += 1
                print('\033[96mFile \'PathWork_join_numbers_usernames.txt\' was created.\033[0m')
        else:
            print('\033[91mНе могу выполнить операцию, создайте файлы с числами и именами.\033[0m')


if __name__ == '__main__':
    path = r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-10'
    test = PathWork(path)
    test.generate_numbers(10)
    test.join_numbers_usernames()
    test.generate_username(15)
    test.join_numbers_usernames()

