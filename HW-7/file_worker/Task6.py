# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from pathlib import Path
from os import chdir
from Task4 import create_file
from random import choice


__all__ = ['get_to_dir']


def get_to_dir(*args, direction=Path().cwd(), how_namy_files: int=1) -> None:
    """Функция генерирует файлы в указанную директорию."""
    if Path(direction).exists():
        chdir(direction)
        for i in range(how_namy_files):
            create_file(choice(args), quantity=1)
    else:
        Path(direction).mkdir(parents=True)
        chdir(direction)
        for i in range(how_namy_files):
            create_file(choice(args), quantity=1)

# Проверку на существование файла добавил в функцию create_file в Task4


if __name__ == '__main__':
    direction = r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\7\ex\tttt'
    get_to_dir('py', how_namy_files=50) #'txt', 'html', 'pdf', 'py', 'mp4', '3gp', 'png', 'java'
