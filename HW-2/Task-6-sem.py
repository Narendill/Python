# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# Печатаем текущий баланс
def balance(summa: float):
    print(f'На вашем счете {round(summa, 2)} у.е.')
    print('___________________________')

# Увеличиваем сумму на 3%
def increase_balance(count_operations: int, summa: float) -> float:
    if count_operations % 3 == 0:
        summa *= 1.03
    return summa

# Проверяем сумму на превышение 5кк
def check_5_bill(summa: float) -> float:
    if summa > 5_000_000:
        summa *= 0.9
    return summa


summa = 0.0
the_end = False
count_operations = 0


balance(summa)
while not the_end:
    to_do = input('Что хотите сделать (пополнить / снять / выйти)? ')
    
    match to_do:
        case 'выйти':
            summa = check_5_bill(summa)
            balance(summa)
            the_end = True
    
        case 'пополнить':
            summa = check_5_bill(summa)
            balance(summa)
            how_much = int(input('Введите сумму пополнения, боольшую, чем ноль и кратную 50 у.е.: '))
            
            while how_much % 50 != 0 or how_much < 0:
                summa = check_5_bill(summa)
                how_much = int(input('Введите сумму пополнения, боольшую, чем ноль и кратную 50 у.е.: '))
            
            summa += how_much
            count_operations += 1
            summa = increase_balance(count_operations, summa)
            balance(summa)
        
        case 'снять':
            summa = check_5_bill(summa)
            balance(summa)
            how_much = int(input('Введите сумму снятия: '))
            
            while how_much % 50 != 0 or how_much > summa or how_much >= summa - 30 or how_much < 0:
                summa = check_5_bill(summa)
                
                if how_much % 50 != 0:
                    print('Вы можете снять сумму, кратную 50 у.е.')
                elif how_much > summa:
                    print('Недостаточно денег на счете.')
                elif how_much > summa - 30:
                    print('За снятие денег взымается комиссия 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. ' +
                          'Недостаточно денег на счете.')
                elif how_much < 0:
                    print('Введите положительное число.')
                
                how_much = int(input('Введите сумму снятия: '))
            
            if how_much == 0:
                print('Вы ничего не сняли.')
            elif how_much * 0.015 < 30:
                summa -= how_much + 30
                count_operations += 1
                summa = round(increase_balance(count_operations, summa), 2)
                print('Комиссия составила 30 у.е.')
            elif how_much * 0.015 > 600:
                summa -= how_much + 600
                count_operations += 1
                summa = round(increase_balance(count_operations, summa), 2)
                print('Комиссия составила 600 у.е.')
            else:
                summa -= how_much * 0.015
                count_operations += 1
                summa = round(increase_balance(count_operations, summa), 2)
                print(f'Комиссия составила {how_much * 0.015} у.е.')
            balance(summa)
