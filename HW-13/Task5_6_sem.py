# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.
import json


class UserException(Exception):
    """Базовое исключение."""
    pass


class LevelError(UserException):
    """Ошибка уровня доступа."""

    def __init__(self, user_lvl, add_lvl):
        self.user_lvl = user_lvl
        self.add_lvl = add_lvl

    def __str__(self):
        if self.user_lvl is None:
            return 'Сначала вам необходимо авторизоваться.'
        elif self.add_lvl <= 0 or self.add_lvl > 7:
            return f'Уровни доступа находятся в пределах [1; 7]. Вы ввели: {self.add_lvl}.'
        elif self.add_lvl < self.user_lvl:
            return 'Недостаточно прав на добавление пользователя.'


class AccessError(UserException):
    """Ошибка входа в систему."""

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f'Пользователь \'{self.name}\' с id = {self.user_id} не существует.'


class User:
    """Класс пользователя."""

    def __init__(self, user_name: str, user_id: int, user_lvl: int):
        """Конструктор класса."""
        self.user_name = user_name
        self.user_id = user_id
        self.user_lvl = user_lvl

    def __str__(self):
        """Строковое представление класса."""
        return f'{self.user_name} {self.user_id} {self.user_lvl}'

    def __eq__(self, other):
        """Проверка на равенство классов."""
        return self.user_name == other.user_name and self.user_id == other.user_id

    def __hash__(self):
        """Создание hash на основании имени пользователя, его id и уровня доступа."""
        return hash((self.user_name, self.user_id, self.user_lvl))


class Project:
    """Класс проекта."""
    __PATH = r'C:\Users\Narendill\Desktop\9_Pogr_in_Python\Seminars\13\user_data.json'

    def __init__(self):
        """Конструктор класса."""
        self.__access_lvl = None
        self.__list_of_users = self.__all_users()

    def get_all_users(self):
        """Метод для себя посмотреть список пользователей."""
        return self.__list_of_users

    def login(self, name: str, user_id: int):
        """Метод входа в систему."""
        temp_user = User(name, user_id, 0)
        for user in self.__list_of_users:
            if user == temp_user:
                self.__access_lvl = user.user_lvl
                return user.user_lvl
        raise AccessError(name, user_id)

    def add_user(self, name, user_id, user_lvl):
        """Метод добавляет пользователя."""
        if (self.__access_lvl is None) or (user_lvl <= 0 or user_lvl > 7) or (user_lvl < self.__access_lvl):
            raise LevelError(self.__access_lvl, user_lvl)
        else:
            self.__list_of_users.add(User(name, user_id, user_lvl))

    def __all_users(self):
        """Метод позволяет получить доступ к базе с пользователями."""
        with open(self.__PATH, 'r', encoding='utf-8') as file:
            result = json.load(file)
        names = set()
        for key_1 in result.keys():
            for key_2 in result[key_1].keys():
                names.add(User(result[key_1][key_2], int(key_2), int(key_1)))
        return names


if __name__ == '__main__':
    a = Project()
    a.login('иван', 15)  # lvl у Ивана 3
    a.add_user('МАКСИМ', 3, 4)  # добавился
    print(*a.get_all_users())
    a.add_user('ИГОРЬ', 99, 2)
    a.add_user('ИГОРЬ', 99, 20)
