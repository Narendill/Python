# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
# doctest, unittest, pytest.

# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import datetime
import unittest


class MyString(str):
    """"В классе доступны все возможности str, дополнительно хранится значение автора строки и время ее создания."""

    def __new__(cls, value, my_name: str):
        """Создание экземпляра класса."""
        instance = super().__new__(cls, value)
        instance.value = value
        instance.my_name = my_name
        instance.my_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return instance

    def __str__(self):
        """Строковое представление экземпляра класса."""
        return f'{self.value}, author: {self.my_name}, time: {self.my_time}'

    def __repr__(self):
        """Формальное строковое представление экземпляра класса."""
        return f'MyString(\'{self.value}\', \'{self.my_name}\')'


class TestMyString(unittest.TestCase):

    def test_repr(self):
        a = MyString('Абырвалг', 'ivanov')
        b = f'{a = }'
        self.assertEqual('a = MyString(\'Абырвалг\', \'ivanov\')', b)

    def test_str(self):
        a = MyString('Абыр', 'ivan')
        self.assertEqual(str(a), f'Абыр, author: ivan, time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}')


if __name__ == '__main__':
    unittest.main(verbosity=2)
