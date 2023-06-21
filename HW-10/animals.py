# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.


class Animal:

    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'{self.name}, {self.age = }, {self.sex = }'

    def add_age(self):
        self.age += 1


class Fish(Animal):

    def __init__(self, name: str, age: int, sex: str, fins: int, speed: int):
        super().__init__(name, age, sex)
        self.fins = fins
        self.speed = speed

    def __str__(self):
        return f'{super().__str__()}, {self.fins = }, {self.speed = } км/ч.'

    def about(self):
        print(f'У меня {self.fins} плавников, и я развиваю скорость {self.speed} км/ч.')


class Bird(Animal):

    def __init__(self, name: str, age: int, sex: str, water: bool):
        super().__init__(name, age, sex)
        self.water = water

    def __str__(self):
        return f'{super().__str__()}, {self.water = }.'

    def about(self):
        like_water = f'водоплавающая' if self.water else 'сухопутная'
        print(f'Я {like_water} птица.')


class Cat(Animal):

    def __init__(self, name: str, age: int, sex: str, paws: int, home: bool):
        super().__init__(name, age, sex)
        self.paws = paws
        self.home = home

    def __str__(self):
        return f'{super().__str__()}, {self.paws = }.'

    def about(self):
        live = f'домашняя' if self.home else 'дикая'
        print(f'Я {live} кошка.')


if __name__ == '__main__':
    print('_' * 30)
    cat = Cat('Tiger', 5, 'male', 4, False)
    print(cat)
    cat.about()
    cat.add_age()
    print(cat)

    print('_' * 30)
    bird = Bird('Sparrow', 2, 'female', False)
    print(bird)
    bird.about()

    print('_' * 30)
    fish = Fish('Salmon', 3, 'male', 7, 40)
    print(fish)
    fish.about()

