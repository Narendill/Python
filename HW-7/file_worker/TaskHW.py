# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from pathlib import Path


__all__ = ['rename_files']


def rename_files(digits: int, ext_old: str, ext_new: str, subname: list, new_name: str='') -> None:
    """Функция переименовывает файлы."""
    counter = 1 # Счетчик для добавления порядкового номера.

    for obj in Path(Path().cwd()).iterdir():
        *_, full_file_name = str(obj).split('\\')
        *_, extension = full_file_name.split('.')
        file_name = full_file_name.split('.')[0]
        if extension == ext_old:
            new_name_full = file_name[subname[0]:subname[1] + 1] + new_name + \
                str(counter).rjust(digits, '0') + '.' + ext_new
            if not Path(new_name_full).exists():
                Path(full_file_name).rename(new_name_full)
                print(f'\033[34mFile \'{full_file_name}\' was renamed as \'{new_name_full}\'.\033[0m')
                counter += 1
                # Сбрасываем счетчик в начальную позицию, чтобы сохранить количество цифр в порядковом номере:
                if counter > int('9' * digits): 
                    counter = 1
            else:
                print(f'\033[33mCouldn\'t rename the file \'{full_file_name}\' to \'{new_name_full}\'',
                'because such file already exists.\033[0m')


if __name__ == '__main__':
    rename_files(2, 'py', 'tmp4', [50, 119], new_name='trtt1')