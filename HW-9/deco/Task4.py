# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
from typing import Callable

__all__ = ['how_many_times']


def how_many_times(num: int = 1):
    def deco(func: Callable):
        result = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return deco


@how_many_times(3)
def _summ(*args) -> int | float:
    return sum(args)


if __name__ == '__main__':
    print(_summ(55, 150))
