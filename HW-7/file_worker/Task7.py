# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения,текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки

from pathlib import Path
from os import chdir


__all__ = ['sort_files']


def sort_files(direcrory=Path().cwd()):
    """Функция сортирует файлы по категориям."""
    types = {
        'images_sorted': ('jpeg', 'jpg', 'png', 'gif'),
        'docs_sorted': ('txt', 'doc', 'docx', 'xls', 'xslx', 'pdf'), 
        'videos_sorted': ('mp4', 'm4v', '3gp'), 
        'prog_files_sorted': ('py', 'java')
            } 
    
    for obj in Path(Path().cwd()).iterdir():
        *_, full_file_name = str(obj).split('\\')
        *_, extension = full_file_name.split('.')

        for key, value in types.items():
            folder_name = Path().cwd() / key
            if extension in value and Path(folder_name).exists():
                obj.replace(Path.cwd() / folder_name / full_file_name)
            elif extension in value and not Path(folder_name).exists():
                Path(folder_name).mkdir()
                obj.replace(Path.cwd() / folder_name / full_file_name)
    print('Sorting was completed.')


if __name__ == '__main__':
    direction = r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\7\ex'
    sort_files(direction)