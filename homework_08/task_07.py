# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
# умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

import math
import pytest


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.__real = float(real)
        self.__imaginary = float(imaginary)

    @property
    def real(self):
        return self.__real

    @property
    def imaginary(self):
        return self.__imaginary

    @property
    def mod(self):
        return math.sqrt(self.__real ** 2 + self.__imaginary ** 2)

    def __str__(self):
        return f'({self.__real} + {self.__imaginary}j)'


    def __add__(self, other):
        return ComplexNumber(self.__real + other.__real, self.__imaginary + other.__imaginary)

    def __mul__(self, other):
        re = self.real * other.real - self.imaginary * other.imaginary
        im = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(re, im)


a = ComplexNumber(3, 4)
print(f'complex: {a}, mod: {a.mod}')
b = ComplexNumber(10, 20)

print(a + b)
print(a * b)

# Сравниваем со стандартными комплексными операциями
print('-'*50)
a= 3+4j
b= 10+20j
print(a+b)
print(a*b)

# ну и pytest конечно

def compare(a, b):
    assert(a.real == b.real)
    assert(a.imaginary == b.imag)

def test_str():
    a = ComplexNumber(3, 4)
    assert(str(a) == '(3.0 + 4.0j)')

def test_mod():
    assert(ComplexNumber(3, 4).mod == 5)

def test_add1():
    a = ComplexNumber(3,4) + ComplexNumber(10, 20)
    b = 3+4j + 10+20j
    compare(a, b)

def test_add2():
    a = ComplexNumber(3, -4) + ComplexNumber(-10, 20)
    b = 3-4j - 10+20j
    compare(a, b)

def test_mul1():
    a = ComplexNumber(3,4) * ComplexNumber(10, 20)
    b = (3+4j) * (10+20j)
    compare(a, b)

def test_mul1():
    a = ComplexNumber(3, -4) * ComplexNumber(-10, 20)
    b = (3-4j) * (-10+20j)
    compare(a, b)


