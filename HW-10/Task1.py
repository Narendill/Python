# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

from animals import Cat, Fish, Bird


class Factory:
    def __init__(self, obj: str, *args, **kwargs):
        self.obj = obj
        self.args = args
        self.kwargs = kwargs

    def create_class(self) -> Cat | Fish | Bird:
        match self.obj:
            case 'Cat':
                return Cat(*self.args, **self.kwargs)
            case 'Fish':
                return Fish(*self.args, **self.kwargs)
            case 'Bird':
                return Bird(*self.args, **self.kwargs)
            case _:
                print(f'\033[91mНе могу создать животного \'{self.obj}\'.\033[0m')


if __name__ == '__main__':
    print('_' * 30)

    sparrow = Factory('Bird', 'Sparrow', 2, sex='female', water=False).create_class()
    print(sparrow)
    print(type(sparrow))

    print('_' * 30)

    swan = Factory('Swan', 'Swan', 2, sex='female', water=False).create_class()
    print(type(swan))
    print(swan)

    print('_' * 30)

    cat = Factory('Cat', 'Murzik', 3, 4,'male', home=True).create_class()
    print(cat)
    print(type(cat))
    cat.about()

    print('_' * 30)
