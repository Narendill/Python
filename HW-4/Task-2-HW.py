# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление

def get_strange_dict(**kwargs) -> dict:
    result = {}
    for key in kwargs.keys():
        if kwargs[key].__hash__ != None:
            result.setdefault(kwargs[key], key)
        else:
            result.setdefault(str(kwargs[key]), key)
    return result

print(get_strange_dict(q=10, w='mother', e=5.5, r=[10, 55],
                       t={12, 3}, y=(10, 'word'), u={10: [11, 0]}))
