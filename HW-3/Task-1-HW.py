# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

def get_double(my_list: list) -> list:
    return list(set([i for i in my_list if my_list.count(i) >= 2]))
    
my_list = [10, 2, 3, 5.5, 'mother', (6, 5), 5.5, 'mother']
print(get_double(my_list))