# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

from pathlib import Path
import csv
import json
from typing import Iterator


__all__ = ['json_to_csv']


def json_to_csv(path: Path | str) -> None:
    path = Path(path)
    with (
        open(path, 'r', encoding='utf-8') as f_read,
        open(f'{Path(path).parent}\\{Path(path).stem}.csv', 'w', encoding='utf-8', newline='') as f_write
    ):

        csv_write = csv.writer(f_write)
        csv_write.writerow(['access', 'id', 'name'])
        f_read = json.load(f_read)
        for key_1 in f_read.keys():
            for key_2, value_2 in f_read[key_1].items():
                to_write_str = [key_1, key_2, value_2]
                csv_write.writerow(to_write_str)
    print(f'\033[36mFile {Path(path).stem}.csv was created.\033[0m')
        

if __name__ == '__main__':
    json_to_csv(r'c:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\8\user_data.json')

