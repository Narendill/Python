# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

import csv
from random import randint


class Fio:
    """Дескриптор для проверки корректности ввода имени и фамилии."""
    def __init__(self):
        self.name = None

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение \'{value}\' должно быть строкой.')
        if not value.isalpha():
            raise TypeError(f'Значение \'{value}\' должно состоять только из букв.')
        if not value.istitle():
            raise TypeError(f'Первая буква в \'{value}\' должна быть прописной, остальные - строчные.')
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')


class Student:
    first_name = Fio()
    last_name = Fio()

    def __init__(self, file_name: str):
        """Конструктор класса."""
        self.__subjects = self.__load_subjects(file_name)
        self.__grades = {subject: {'marks': [], 'tests': []} for subject in self.__subjects}

    def __load_subjects(self, file_name: str):
        """Метод загрузки списка предметов."""
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            subjects = []
            for row in reader:
                subjects += row
        return subjects

    def set_mark(self, subject: str, mark: int):
        """Вносит оценку за предмет."""
        if subject not in self.__subjects:
            raise ValueError('Такого предмета не существует.')
        if not (2 <= mark <= 5):
            raise ValueError("Оценка должна быть в диапазоне от 2 до 5")
        if not isinstance(mark, int):
            raise ValueError("Оценка должна быть целым числом.")
        self.__grades[subject]['marks'].append(mark)

    def set_test(self, subject: str, mark: int):
        """Вносит оценку за тест."""
        if subject not in self.__subjects:
            raise ValueError('Такого предмета не существует.')
        if not (0 <= mark <= 100):
            raise ValueError("Оценка должна быть в диапазоне от 0 до 100")
        if not isinstance(mark, int):
            raise ValueError("Оценка должна быть целым числом.")
        self.__grades[subject]['tests'].append(mark)

    def average_test_mark(self, subject: str):
        """Возвращает среднее значение по тестам для конкретного предмета."""
        marks = self.__grades[subject]['tests']
        return round(sum(marks) / len(marks), 2) if marks else 0

    def average_marks_all_subjects(self):
        """Возвращает среднее значение по всем оценкам всех предметов."""
        marks = [mark for subject in self.__subjects for mark in self.__grades[subject]['marks']]
        return round(sum(marks) / len(marks), 2) if marks else 0

    def __str__(self):
        """Строковое представление экземпляра класса."""
        return f'{self.last_name} {self.first_name}:\n' \
               + '_' * 50 + '\n' \
               + '\n'.join(f'{key}: {value}' for key, value in self.__grades.items()) + '\n' \
               + '_' * 50 + '\n'


if __name__ == '__main__':
    ivan = Student('subjects.csv')
    ivan.first_name = 'Иван'
    ivan.last_name = 'Иванов'

    for mark in range(2, 6):
        ivan.set_mark('History', mark)
    for mark in range(3, 6):
        ivan.set_mark('Math', mark)
    for mark in range(10):
        ivan.set_test('Math', randint(0, 100))

    print(ivan)
    print(ivan.average_test_mark('Math'))
    print(ivan.average_marks_all_subjects())


