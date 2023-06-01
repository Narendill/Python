# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список

# Печатаем текущий баланс
def balance(summa: float):
    print(f'На вашем счете {round(summa, 2)} у.е.')
    print('_' * 30)


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


# Проверка корректности снятия денег
def check_withdraw(how_much: int):
    if how_much % 50 != 0:
        print('Вы можете снять сумму, кратную 50 у.е.')
    elif how_much > summa:
        print('Недостаточно денег на счете.')
    elif how_much > summa - 30:
        print('За снятие денег взымается комиссия 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. ' +
            'Недостаточно денег на счете.')
    elif how_much < 0:
        print('Введите положительное число.')
        
        
summa = 0.0
the_end = False
count_operations = 0
operations = [] # Храним снятие / пополнение


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
            
            operations.append(how_much)
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
                check_withdraw(how_much)
                how_much = int(input('Введите сумму снятия: '))
            
            if how_much == 0:
                print('Вы ничего не сняли.')
            elif how_much * 0.015 < 30:
                operations.append(-how_much)
                summa -= how_much + 30
                count_operations += 1
                summa = round(increase_balance(count_operations, summa), 2)
                print('Комиссия составила 30 у.е.')
            elif how_much * 0.015 > 600:
                operations.append(-how_much)
                summa -= how_much + 600
                count_operations += 1
                summa = round(increase_balance(count_operations, summa), 2)
                print('Комиссия составила 600 у.е.')
            else:
                operations.append(-how_much)
                summa -= how_much * 0.015
                count_operations += 1
                summa = round(increase_balance(count_operations, summa), 2)
                print(f'Комиссия составила {how_much * 0.015} у.е.')
            balance(summa)
print('Произведенные операции: ', operations)
