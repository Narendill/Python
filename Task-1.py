# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

message = 'Enter the length of the side of the triangle: '
a, b, c = int(input(message)), int(input(message)), int(input(message))

if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        print('Equilateral triangle.')
    elif a == b or a == c or b == c:
        print('Isosceles triangle.')
    else:
        print('Scalene triangle.')
else:
    print('Triangle does not exist.')
