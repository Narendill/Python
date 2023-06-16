# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv
from pathlib import Path


__all__ = ['pickle_to_csv']


def _matrix_transpose(matrix: list) -> list:
    """Функция транспонирует матрицу"""
    matrix_new = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            matrix_new[i][j] = matrix[j][i]
    return matrix_new


def pickle_to_csv(path: Path | str) -> None:
    path = Path(path)
    with (
        open(path, 'rb') as f_read,
        open(f'{Path(path).parent}\\{Path(path).stem}.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        f_read = pickle.load(f_read)
        
        # Заголовки
        headers = [key for i in f_read for key in i.keys()]

        # Содержимое
        result = []
        for i in f_read:
            for j in i.values():
                result.append(j)
        # Транспонируем
        result = _matrix_transpose(result)

        # Записываем
        csv_write = csv.writer(f_write)
        csv_write.writerow(headers)
        csv_write.writerows(result)

        print(f'\033[36mFile {Path(path).stem}.csv was created.\033[0m')


if __name__ == '__main__':
    pickle_to_csv(r'c:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\8\task4.pickle')