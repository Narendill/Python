# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

from random import randint, choice, randbytes
from string import ascii_letters
from pathlib import Path


__all__ = ['create_file']


def create_file(extension: str, min_name: int=6, max_name: int=30, \
    min_byte: int=256, max_byte: int=4096, quantity: int=42) -> None:
    """Функция генерирует файлы с указанным расширением."""
    iterations = 0
    while iterations < quantity:
        name = ''
        for i in range(randint(min_name, max_name)):
            name += choice(ascii_letters)
        name += '.' + extension

        # Добавил проверку на то, существует ли файл
        absolut_name = Path().cwd() / name
        if not Path(absolut_name).exists():
            with open(name, 'w+b') as f:
                how_many_bytes = randint(min_byte, max_byte)
                f.write(randbytes(how_many_bytes))
            print(f'File \"{name}\" was created. len(name) = {len(name) - len(extension)},',
                f'size = {how_many_bytes}')
            iterations += 1


if __name__ == '__main__':
    create_file('txt', quantity=40)