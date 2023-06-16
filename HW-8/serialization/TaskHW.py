# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import json
import csv
import pickle
from pathlib import Path


__all__ = ['get_files']


def _folder_size(path: Path) -> int:
    """Функция возвращает размер папки / файла в байтах."""
    size = 0
    if Path(path).is_file():
        return Path(path).stat().st_size

    get_list_dir = Path(path).iterdir()
    for obj in get_list_dir:
        if obj.is_file():
            size += obj.stat().st_size
        else:
            size += _folder_size(obj)
    return size


def _get_info(path: Path | str=Path.cwd()) -> None:
    """Функция возвращает список с информацией о типе объекта, его размере и родительской папке."""
    direction = Path(path)
    get_list_dir = Path(direction).iterdir()
    result = []

    for obj in get_list_dir:
        *_, parent = str(obj.parent).split('\\') # Определяем родительскую папку
        _type = 'Folder' if obj.is_dir() else 'File' # Определяем файл или папка
        result.append({obj.name: [_type, parent, _folder_size(obj)]})
        if obj.is_dir():
            result.extend(_get_info(obj))
    
    return result

def get_files(path: Path | str=Path.cwd()) -> None:
    """Функция записывает информацию о содержимом папки в файлы json, csv и pickle."""
    # Прверка на то, является ли путь директорией
    direction = Path(path)
    if not direction.is_dir():
        print(f'\033[31m{path} is not a directory.\033[0m')
        return

    result = _get_info(path) # Получаем информацию о содержимом папки
    # Запись файлов
    with (
        open(f'{Path(path).parent}\\{Path(path).stem}.json', 'w') as f_json,
        open(f'{Path(path).parent}\\{Path(path).stem}.csv', 'w', newline='') as f_csv, 
        open(f'{Path(path).parent}\\{Path(path).stem}.pickle', 'wb') as f_pickle, 
    ):
        # Запись json
        json.dump(result, f_json, ensure_ascii=False, indent=2)
        print(f'\033[36mFile {Path(path).stem}.json was created.\033[0m')

        # Запись csv
        csv_write = csv.writer(f_csv)
        csv_write.writerow(['name', 'type', 'parent', 'size']) # Столбцы
        for row in result:
            filename = list(row.keys())[0]
            values = row[filename]
            csv_write.writerow([filename, values[0], values[1], values[2]])
        print(f'\033[36mFile {Path(path).stem}.csv was created.\033[0m')

        # Запись pickle
        pickle.dump(result, f_pickle)
        print(f'\033[36mFile {Path(path).stem}.pickle was created.\033[0m')


if __name__ == '__main__':
    get_files(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\8')


