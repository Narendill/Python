# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def get_path(link: str) -> tuple:
    link_list = link.split('/')
    
    file_path = '/'.join(link_list[0:-1])
    file_name = link_list[-1].split('.')[0]
    file_extension = link_list[-1].split('.')[1]
    
    return file_path, file_name, file_extension


link = 'C:/Users/Narendill/Desktop/9_Pogr_in_Python/HW/HW-1/Task-1.py'
print(get_path(link))