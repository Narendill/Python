# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction
from math import gcd


def mult(num1: list, num2: list):
    
    numerator = num1[0] * num2[0]
    denominator = num1[1] * num2[1]
    _gcd = gcd(numerator, denominator) # наибольший общий делитель для сокращения
    
    print(f'{num1[0]}/{num1[1]} * {num2[0]}/{num2[1]} = {int(numerator / _gcd)}/{int(denominator / _gcd)}')


def summa(num1: list, num2: list):
    
    denominator = num1[1] * num2[1]
    numerator = num1[0] * num2[1] + num2[0] * num1[1]
    _gcd = gcd(numerator, denominator) # наибольший общий делитель для сокращения
    
    print(f'{num1[0]}/{num1[1]} + {num2[0]}/{num2[1]} = {int(numerator / _gcd)}/{int(denominator / _gcd)}')


num1 = [int(i) for i in input('Введите первую дробь: ').split('/')]
num2 = [int(i) for i in input('Введите вторую дробь: ').split('/')]

mult(num1, num2)
summa(num1, num2)

# Проверка
print('____________________')
print('Проверка:')
print(Fraction(num1[0], num1[1]) * Fraction(num2[0], num2[1]), \
    Fraction(num1[0], num1[1]) + Fraction(num2[0], num2[1]))
