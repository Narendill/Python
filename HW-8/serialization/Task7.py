# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
from pathlib import Path
import pickle


__all__ = ['print_csv_to_pickle']


def print_csv_to_pickle(path: Path | str) -> None:
    path = Path(path)
    with open(path, 'r', encoding='utf-8', newline='') as f_read:
        print(pickle.dumps(list(csv.reader(f_read))))
        

if __name__ == '__main__':
    print_csv_to_pickle(r'c:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\8\task4.csv')