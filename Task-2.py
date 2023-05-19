# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input('Enter a number between 0 and 100 000: '))
LOWER_LIMIT = 0
UPPER_LIMIT = 100_000


while num < LOWER_LIMIT or num > UPPER_LIMIT:
    num = int(input('Enter a number between 0 and 100000: '))
    
if num == 0 or num == 1:
    print(f'You entered {num}. It is neither a prime nor a composite number.')
else:
    prime = True
    i = 2
    while i <= num**0.5:
        if num % 2 == 0:
            prime = False
            break
        i += 1
    if prime:
        print('Prime number.')
    else:
        print('Composite number.')