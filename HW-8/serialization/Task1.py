# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
from pathlib import Path

__all__ = ['txt_to_json']


def txt_to_json(path: Path | str) -> None:
    """Функция создает json файл на основании имеющегося."""
    path = Path(path)
    with(
        open(path, 'r', encoding='utf-8') as f_read,
        open(f'{Path(path).parent}\\{Path(path).stem}.json', 'w', encoding='utf-8') as f_write
    ):
        result = {}
        for line in f_read.readlines():
            result.setdefault(line.split()[0].capitalize(), round(float(line.split()[1]), 2))
        json.dump(result, f_write, ensure_ascii=False, indent=0)
        print(f'\033[36mFile {Path(path).stem}.json was created.\033[0m')


if __name__ == '__main__':
    txt_to_json(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-8\example_1.txt')