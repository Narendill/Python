# Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня

def equation_solution(a: int, b: int, c: int) -> list:
    
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / 2 / a
        x2 = (-b - discriminant**0.5) / 2 / a
    elif discriminant == 0:
        x1 = -b / 2 / a
        return [x1]
    else:
        x1 = (-b + complex(discriminant**0.5)) / 2 / a
        x2 = (-b - complex(discriminant**0.5)) / 2 / a
    return [x1, x2]

print(equation_solution(3, -18, 27)) # Один корень
print(equation_solution(3, -18, 7)) # Два корня
print(equation_solution(3, -18, 270)) # Два комплексных корня