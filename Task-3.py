# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
iteration = 0

while iteration < 10:
    print(f'Try #{iteration+1}')
    answer = int(input('Guess the number:'))
    if answer == num:
        print('You right!')
        iteration = 10
    elif answer > num:
        print('Too much.')
        iteration += 1
    else:
        print('Need more.')
        iteration += 1
print(f'Correct answer is {num}.')