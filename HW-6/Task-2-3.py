# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
# для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки.

from random import randint


def eight_queens(coordinates: list[tuple[int]]) -> bool:
    """Функция определяет могут ли 8 ферзей бить друг друга."""
    result = []

    for i in range(len(coordinates) - 1):
        for j in range(i+1, len(coordinates)):
            # Проверяем не стоят ли ферзи на одинаковых горизонтальных / вертикальных  линиях.
            if coordinates[i][0] == coordinates[j][0] or coordinates[i][1] == coordinates[j][1]:
                result.append(False)
            # Проверяем не стоят ли ферзи на одинаковых диагоналях.
            elif abs(coordinates[i][0] - coordinates[j][0]) == abs(coordinates[i][1] - coordinates[j][1]):
                result.append(False)
            else:
                result.append(True)
    
    if False in result:
        return False
    else:
        return True


def print_chessboard(coordinates: list[tuple[int]]) -> None:
    """Функция печатает шахматную доску с 8-ю ферзями."""
    print()
    print(' ', *[f'{i} ' for i in range(1, 9)])
    for i in range(1, 9):
        print(f'{i} ', end='')
        for j in range(1, 9):
            counter = 0
            for k in coordinates:
                if k[0] == i and k[1] == j:
                    print('♕  ', end='')
                    counter += 1
            if counter == 0:
                print('☐  ', end='')
            counter = 0
        print(end='\n')
    print()


def get_perfect_positions(how_much: int=4) -> dict[int: list[tuple[int]]]:
    """Функция определяет 4 позиции 8-ми ферзей, при которых они не бьют друг друга."""
    success = 0
    result = {} # В словаре храним "успешные" комбинации.
    while success < how_much:
        positions = [(randint(1, 8), randint(1, 8)) for i in range(8)]
        if eight_queens(positions): # Проверяем бьют ли ферзи друг друга.
            print(positions)
            success += 1
            print_chessboard(positions) # Печатаем доску.
            result.setdefault(success, positions)
    return result



if __name__ == '__main__':
    # Комбинация где не бьют
    coordinates_1 = [(1, 4), (2, 2), (3, 8), (4, 5), (5, 7), (6, 1), (7, 3), (8, 6)]
    print_chessboard(coordinates_1)
    print(eight_queens(coordinates_1))

    # Комбинация где бьют
    coordinates_2 = [(1, 4), (2, 2), (3, 8), (4, 5), (5, 7), (6, 1), (7, 3), (8, 8)]
    print_chessboard(coordinates_2)
    print(eight_queens(coordinates_2))

    # Найдем одну расстановку (а то 4 слишком долго).
    print(get_perfect_positions(how_much=1))

    
