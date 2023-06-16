# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
from pathlib import Path

__all__ = ['write_data']

_MIN_LVL_ACCESS = 1
_MAX_LVL_ACCESS = 7


def write_data(path: Path | str):
    """Функция запрашивает личные данные пользователя
     и записывает введенные пользователем данные в json-файл.
    """
    path = Path(path)
    # Проверяем существует ли файл, чтобы корретно вносить в него изменения
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            total_result = json.load(f, object_hook=lambda x: {int(key): value for key, value in x.items()})
    else:
        # Создаем пустой словарь с уровнями доступа в ключах
        total_result = {key: {} for key in range(_MIN_LVL_ACCESS, _MAX_LVL_ACCESS + 1)}

    # Пользовательский ввод
    while True:
        user_name = input('Введите свое имя: ')
        user_id = int(input('Введите свой ID: '))
        user_lvl_access = int(input('Введите свой уровень доступа от 1 до 7: '))
        # Проверка корректности ввода уровня доступа
        while user_lvl_access < _MIN_LVL_ACCESS or user_lvl_access > _MAX_LVL_ACCESS:
            user_lvl_access = int(input('Введите свой уровень доступа от 1 до 7: '))
       
        # Проверка на наличие ID в словаре и апдейт словаря
        for value in total_result.values():
            if user_id in value.keys():
                value.pop(user_id) 
        total_result[user_lvl_access].update({user_id: user_name})
        
        # Запись в файл
        with open(f'{Path(path).parent}\\{Path(path).stem}.json', 'w') as f_write:
            json.dump(total_result, f_write, ensure_ascii=False, indent=2)
        

if __name__ == '__main__':
    write_data(r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\HW\HW-8\task2.json')