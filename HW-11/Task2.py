# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Архив хранит два свойства: число и строку. Все данные, переданные в создаваемые экземпляры класса хранятся в
    атрибуте list_archive. """
    list_archive = []

    def __new__(cls, num: int, text: str):
        """Сохраняет в атрибут list_archive переданные аргументы."""
        instance = super().__new__(cls)
        instance.list_archive.append([num, text])
        return instance

    def __init__(self, num: int | float, text: str):
        """Добавляет два атрибута: num и text."""
        self.num = num
        self.text = text

    def __str__(self):
        """Строковое представление экземпляра класса."""
        return f'({self.num}, \'{self.text}\', {self.list_archive})'

    def __repr__(self):
        """Формальное строковое представление экземпляра класса."""
        return f'Archive({self.num}, \'{self.text}\')'


if __name__ == '__main__':
    a = Archive(10, 'rrr')
    b = Archive(20, 'qqq')
    print(a)
    print(repr(a))
    # print(help(a))

