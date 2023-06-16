# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

from pathlib import Path
import csv
import json


__all__ = ['csv_to_json']


def csv_to_json(path: Path | str, name_end: str) -> None:
    path = Path(path)
    with (
        open(path, 'r', encoding='utf-8') as f_read,
        open(f'{Path(path).parent}\\{name_end}', 'w', encoding='utf-8',) as f_write
    ):
        result = []
        f_read = list(csv.reader(f_read))

        for i in range(1, len(f_read)):
            val = []
            val.append(f_read[i][0])
            val.append(f'{str(0) * (10 - len(f_read[i][1]))}{f_read[i][1]}')
            val.append(f_read[i][2].capitalize())
            result.append({f_read[i][1] + f_read[i][2]: val})

        json.dump(result, f_write, ensure_ascii=False, indent=2)
       
        print(f'\033[36mFile {name_end} was successfully created.\033[0m')


if __name__ == '__main__':
    csv_to_json(r'c:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\8\user_data.csv', 'task4')
