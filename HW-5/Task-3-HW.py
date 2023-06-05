# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci_sequence():
    f_1 = 0
    f_2 = 1
    while True:
        yield f_1
        temp = f_1
        f_1 = f_2
        f_2 = temp + f_1

# Напечатаем первые 15 чисел последовательности
count = 0
for i in fibonacci_sequence():
    print(i, end=' ')
    count += 1
    if count == 15:
        break
