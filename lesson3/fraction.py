"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:

    def __init__(self, numerator: int, denominator: int):
        self.numerator: int = numerator
        self.denominator: int = denominator

    def __repr__(self):
        return f'{self.__class__.__name__}({self.numerator}, {self.denominator})'

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other: 'Fraction') -> 'Fraction':
        if not isinstance(other, Fraction):
            raise TypeError('other must be Fraction')

        res = Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                       self.denominator * other.denominator)  # 10 / 8

        divider = self.gcd(res.numerator, res.denominator)

        res = Fraction(res.numerator // divider, res.denominator // divider)
        return res

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """ Наибольший общий делитель """
        while b:
            a, b = b, a % b
        return a


fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
