# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл


from random import randint, choice


__all__ = ['generate_username']
_VOWLES = 'ёуеыаоэяию'
_CONS = 'йцкнгшщзхфвпрлджчсмтб'
_MIN = 4
_MAX = 7


def generate_username(count: int=1) -> None:
    """Функция генерирует случайные имена и сохраняет их в файл usernames.txt"""
    iteration = 0

    with open('usernames.txt', 'a', encoding='utf-8') as f:
        while iteration < count:
            result = '' # Храним имя.
            choose = randint(0, 1) # Выбираем с гласной или согласной начинаем имя.
            how_many_letters = randint(_MIN, _MAX)

            for i in range(how_many_letters):
                if choose == 0:
                    result += choice(_VOWLES)
                    choose = 1
                else:
                    result += choice(_CONS)
                    choose = 0
            iteration += 1
            print(result.capitalize(), file=f)


if __name__ == '__main__':
    generate_username(10)