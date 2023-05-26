# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

with open('constitution.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

# Удаляем все символы кроме букв и пробелов. Перводим всё в нижний регистр.
text_new = ''
for i in text:
    if i.isalpha() or i.isspace():
        text_new += i.lower()

# Делаем список слов и множество уникальных слов в тексте
words = text_new.split()
set_words = set(words)

# Создаем словарь и подсчитываем частоту слов
dict_words = {}
for i in set_words:
    dict_words.setdefault(i, words.count(i))

# Сортируем словарь по количеству повторений слов
sorted_dict = dict(sorted(dict_words.items(), reverse=True, key=lambda item: item[1]))

# Выводим 10 наиболее часто втречающихся слов
iterations = 0 
for key, value in sorted_dict.items():
    print(f'{key:>15} - {value}')
    iterations += 1
    
    if iterations == 10:
        break
