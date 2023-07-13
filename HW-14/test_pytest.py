# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
# doctest, unittest, pytest.


# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

import pytest


class UserException(Exception):
    pass


class NegativeValue(UserException):
    """Проверка корректности ввода сторон треугольника."""

    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if not all(isinstance(side, (int, float)) for side in [self.a, self.b, self.c]):
            return 'Стороны треугольника должны иметь тип \'int\' или \'float\'.'
        elif any(side <= 0 for side in [self.a, self.b, self.c]):
            return 'Сторона треугольника не может быть меньше или равной нулю.'
        else:
            return 'Треугольник не существует.'


class Triangle:

    def __init__(self, a: int | float, b: int | float, c: int | float):
        """Конструктор класса."""
        if not all(isinstance(side, (int, float)) for side in [a, b, c]) or any(side <= 0 for side in [a, b, c]) or (
                a + b <= c or a + c <= b or c + b <= a):
            raise NegativeValue(a, b, c)
        self.a = a
        self.b = b
        self.c = c
        self.__type_triangle = self.__triangle_type()

    @property
    def type(self):
        """Возвращает тип треугольника."""
        return self.__type_triangle

    def __triangle_type(self):
        if self.a == self.b == self.c:
            return 'равносторонний'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'равнобедренный'
        elif max(self.a, self.b, self.c) ** 2 == min(self.a, self.b, self.c) ** 2 + (
                self.a + self.b + self.c - max(self.a, self.b, self.c) - min(self.a, self.b, self.c)) ** 2:
            return 'прямоугольный'
        else:
            return 'разносторонний'

    def __str__(self):
        """Строковое представление треугольника - кортеж из трех его сторон."""
        return f'({self.a}, {self.b}, {self.c})'


# _____________________________________________________________________________________
# ТЕСТИРОВАНИЕ
def test_triangle_type_1():
    assert Triangle(10, 10, 10).type == 'равносторонний'


def test_triangle_type_2():
    assert Triangle(10, 10, 15).type == 'равнобедренный'


def test_triangle_type_3():
    assert Triangle(3, 4, 5).type == 'прямоугольный'


def test_triangle_type_4():
    assert Triangle(10, 9, 8).type == 'разносторонний'


def test_str():
    assert str(Triangle(10, 10, 10)) == '(10, 10, 10)'


def test_type_params_1():
    with pytest.raises(NegativeValue, match='Стороны треугольника должны иметь тип \'int\' или \'float\'.'):
        Triangle(10, 10, 'mother')


def test_type_params_2():
    with pytest.raises(NegativeValue, match='Стороны треугольника должны иметь тип \'int\' или \'float\'.'):
        Triangle(10, 10, (10, 10))


def test_negative_side():
    with pytest.raises(NegativeValue, match='Сторона треугольника не может быть меньше или равной нулю.'):
        Triangle(-10, -10, -10)


def test_triangle_exists():
    with pytest.raises(NegativeValue, match='Треугольник не существует.'):
        Triangle(2, 1, 4)


if __name__ == '__main__':
    pytest.main(['-v'])
