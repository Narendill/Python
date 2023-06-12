# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import choice
from Task4 import create_file


__all__ = ['create_file_extension']


def create_file_extension(*args, how_namy_files: int=1) -> None:
    """Функция генерирует файлы с различными расширениями."""
    for i in range(how_namy_files):
        create_file(choice(args), quantity=1)
    

if __name__ == '__main__':
    create_file_extension('txt', 'doc', 'py', 'html', 'csv', how_namy_files=10)