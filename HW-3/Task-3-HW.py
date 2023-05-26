# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import itertools


def backpack(things: dict):
    CAPACITY = 10

    permutations = list(itertools.permutations(things.keys())) # Создаем всевозможные комбинации для рюкзака без учета веса
    summ = 0 # Переменная для проверки веса помещаемых в рюкзак вещей
    things_tuple = () # В этот кортеж будем складывать вещи, которые помещаются в рюкзак
    things_set = set() # В множестве будем хранить  кортежи всевозможных комбинаций сборки рюкзака


    for permutation in permutations:
        for i in range(len(permutation)):
            if summ < 10 and summ + things[permutation[i]] <= CAPACITY:
                summ += things[permutation[i]]
                things_tuple += (permutation[i],)
        # Сортируем кортеж (чтобы в множестве не встречалось одно и тоже в разном порядке)
        # типа (картошка, вода) и (вода, картошка) и добалвяем его в множество
        
        things_set.add(tuple(sorted(things_tuple)))
        things_tuple = ()
        summ = 0

    print('_______________________________________________________________________')
    print(f'Всевозможные комбинации укладки рюкзака с максимальной массой в {CAPACITY} кг.:')
    print('_______________________________________________________________________')
    for i in things_set:
        summa = 0
        for j in range(len(i)):
            summa += things[i[j]]
        print(f'{i} - {summa} кг.')
    print('_______________________________________________________________________')
    
things = {'картошка': 2,
          'консервы': 4,
          'фонарик': 1,
          'вода': 2,
          'котелок': 3,
          'теплые вещи': 3,
          }
backpack(things)
