# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import pickle
from pathlib import Path
import json

__all__ = ['json_to_pickle']


def json_to_pickle(path: Path | str) -> None:
    path = Path(path)
    file_names = [file.name for file in Path(path).iterdir() \
        if file.is_file() and str(file).endswith('.json')]

    for file in file_names:
        with (
            open(Path(path) / file, 'r', encoding='utf-8') as f_read,
            open(f'{Path(path)}\\{Path(file).stem}.pickle', 'wb') as f_write
        ):
            f_read = json.load(f_read)
            pickle.dump(f_read, f_write)

            print(f'\033[36mFile {Path(file).stem}.pickle was created.\033[0m')


if __name__ == '__main__':
    json_to_pickle(r'c:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\8')