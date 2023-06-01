# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце

def rename_var():
    dict_vars = globals()
    new_vars = {}
    for key in dict_vars.keys():
        if key.endswith('s') and len(key) > 1:
            new_vars.setdefault(key[:-1], dict_vars[key])
            dict_vars[key] = None
    dict_vars.update(new_vars)
   
            
names = 10
res = 'mother'
s = 5.5
result = 15
income = 333
dates = [10, 20, -5]

print('Было:')
print(f'{names = }, {res = }, {s = }, {result = }, {income = }, {dates = }')
rename_var()
print('Стало:')
print(f'{names = }, {res = }, {s = }, {result = }, {income = }, {dates = }')
print('_' * 80)
print('Проверим сохранились ли переменные без -s:')
print(globals())
