# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    """Класс Matrix представляет матрицы и предоставляет операции над ними."""

    def __init__(self, matrix: list[list[int | float]]):
        """Инициализирует матрицу."""
        length_row = len(matrix[0])
        for row in matrix:
            if len(row) != length_row:
                raise ValueError("Матрица введена некорректно.")  # Защита от ввода типа [[1, 2, 3], [1, 2]]
        self.matrix = matrix

    def __add__(self, other: 'Matrix'):
        """Складывает две матрицы одинакового размера."""
        result = []
        can_summ = True
        # Проверяем равенство строк и столбцов в матрицах:
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    can_summ = False
        else:
            can_summ = False
        # Суммируем матрицы:
        if can_summ:
            to_add = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    to_add.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(to_add)
                to_add = []
            return Matrix(result)
        else:
            raise ValueError("Размеры матриц не совпадают.")

    def __mul__(self, other: 'Matrix'):
        """Умножает две матрицы друг на друга."""
        # Умножать матрицы можно, если их размерность (l x m) и (m x n) -> (l x n)
        if len(self.matrix[0]) == len(other.matrix):
            result = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(result)
        else:
            raise ValueError("Несовместимые размеры матриц для умножения.")

    def __eq__(self, other: 'Matrix'):
        """Проверяет, равны ли две матрицы."""
        equal = True
        # Проверяем равенство строк и столбцов в матрицах:
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    equal = False
                    return equal
                else:
                    for j in range(len(self.matrix[i])):  # Проверяем равенство элементов
                        if self.matrix[i][j] != other.matrix[i][j]:
                            equal = False
                            return equal
        else:
            equal = False
        return equal

    # Остальные операции сравнения над матрицами не определены
    def __gt__(self, other):
        raise TypeError("Операция > не поддерживается")

    def __ge__(self, other):
        raise TypeError("Операция >= не поддерживается")

    def __lt__(self, other):
        raise TypeError("Операция < не поддерживается")

    def __le__(self, other):
        raise TypeError("Операция <= не поддерживается")

    def __str__(self):
        """Строковое представление матрицы."""
        result = '\n'
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result += f'{self.matrix[i][j]:<7}'
            result += '\n'
        return result

    def __repr__(self):
        """Формальное строковое представление экземпляра класса."""
        return f'Matrix({self.matrix})'


if __name__ == '__main__':
    my_list_1 = [[10, 20, 30], [40, 50, 60]]
    my_list_2 = [[1, 1, 1], [1, 1, 9]]
    my_list_3 = [[10, 20], [40, 50], [1, 1]]
    a = Matrix(my_list_1)
    b = Matrix(my_list_2)
    c = Matrix(my_list_3)
    print(repr(a))
    print(f'{a = }')
    print(a)

    d = a + b
    print(d)

    q = a * c
    print(q)

    print(a == c)
    print(a > b)
