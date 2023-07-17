# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
import logging
from collections import namedtuple
from pathlib import Path


Dir = namedtuple('Dir', ['name', 'extension', 'type', 'parent'])


def directory_info(path: Path | str = Path.cwd()) -> list:
    """Функция возвращает список с информацией о типе объекта, его размере и родительской папке."""
    direction = Path(path)
    get_list_dir = Path(direction).iterdir()
    result = []

    for obj in get_list_dir:
        *_, parent = str(obj.parent).split('\\')  # Определяем родительскую папку
        _type = 'Folder' if obj.is_dir() else 'File'  # Определяем файл или папка
        suffix = obj.suffix if obj.suffix != '' else None  # Определяем расширение
        result.append(Dir(obj.stem, suffix, _type, parent))
        logger.info(Dir(obj.stem, suffix, _type, parent))
        if obj.is_dir():
            result.extend(directory_info(obj))

    return result


if __name__ == '__main__':
    logging.basicConfig(filename='dir_info.log', level=logging.NOTSET, encoding='utf-8',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='Парсер содержимого папки.')
    parser.add_argument('-url', metavar='url', type=str, help='Введите путь к папке.', default=Path.cwd())
    args = parser.parse_args()

    print(*directory_info(args.url), sep='\n')
    print('\033[94mВсе информация о содержимом директории сохранена в файл \'dir_info.log\'.\033[0m')
