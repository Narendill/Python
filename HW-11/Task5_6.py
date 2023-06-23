# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади.
# Должны работать все шесть операций сравнения.

class Rectangle:
    """Класс хранит стороны прямоугольника."""

    def __init__(self, length: int | float, wide: int | float = None):
        """Создание экземпляра класса."""
        self.length = length
        self.wide = wide
        if self.wide is None:
            self.wide = self.length

    def perimeter(self) -> float:
        """Вычисление периметра прямоугольника."""
        if self.wide is not None:
            return (self.length + self.wide) * 2
        else:
            return self.length * 4

    def area(self) -> float:
        """Вычисление площади прямоугольника."""
        if self.wide is not None:
            return self.length * self.wide
        else:
            return self.length ** 2

    def __add__(self, other):
        """Сложение двух прямоугольников."""
        perimetr_in_add = self.perimeter() + other.perimeter()
        return Rectangle(self.length, perimetr_in_add / 2 - self.length)

    def __sub__(self, other):
        """Разность двух прямоугольников."""
        perimetr_in_add = abs(self.perimeter() - other.perimeter())
        return Rectangle(self.length, abs(perimetr_in_add / 2 - self.length))

    def __eq__(self, other):
        """Проверка равенства двух прямоугольников."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Проверка неравенства друх прямоугольников."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Проверка больше ли один прямоугольник другого."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Проверка больше или равен ли один прямоугольник другого."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Проверка меньше ли один прямоугольник другого."""
        return self.area() < other.area()

    def __le__(self, other):
        """Проверка меньше или равен ли один прямоугольник другого."""
        return self.area() <= other.area()

    def __str__(self):
        """Строковое представление экземпляра класса."""
        return f'({self.length}, {self.wide})'

    def __repr__(self):
        """Формальное строковое представление экземпляра класса."""
        return f'Rectangle({self.length}, {self.wide})'


if __name__ == '__main__':
    rectangle_1 = Rectangle(10)
    rectangle_2 = Rectangle(10, 5)
    print(f'{rectangle_1.perimeter() = }, {rectangle_2.perimeter() = }')
    print(rectangle_1 + rectangle_2)
    print(rectangle_1 - rectangle_2)
    print(rectangle_1.area(), rectangle_2.area())
    print('==', rectangle_1 == rectangle_2)
    print('!=', rectangle_1 != rectangle_2)
    print('>', rectangle_1 > rectangle_2)
    print('>=', rectangle_1 >= rectangle_2)
    print('<', rectangle_1 < rectangle_2)
    print('<=', rectangle_1 <= rectangle_2)
    print(rectangle_1)
    print(repr(rectangle_1))
