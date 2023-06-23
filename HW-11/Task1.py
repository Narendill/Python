# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import datetime


class MyString(str):
    """"В классе доступны все возможности str, дополнительно хранится значение автора строки и время ее создания."""

    def __new__(cls, value, my_name: str):
        """Создание экземпляра класса."""
        instance = super().__new__(cls, value)
        instance.value = value
        instance.my_name = my_name
        instance.my_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return instance

    def __str__(self):
        """Строковое представление экземпляра класса."""
        return f'{self.value}, author: {self.my_name}, time: {self.my_time}'

    def __repr__(self):
        """Формальное строковое представление экземпляра класса."""
        return f'MyString(\'{self.value}\', \'{self.my_name}\')'


if __name__ == '__main__':
    a = MyString('Абырвалг', 'ivanov')
    print(a)
    print(repr(a))
