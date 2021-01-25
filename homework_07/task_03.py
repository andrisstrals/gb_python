# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
#     сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
#
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
#    двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

import pytest

class Cell:
    def __init__(self, cells):
        self.__numcells = int(cells)

    @property
    def numcells(self):
        return self.__numcells

    def __str__(self) -> str:
        return f'Cell({self.__numcells})'

    def __eq__(self, other) -> bool:
        return self.__numcells == other.__numcells

    def __add__(self, other):
        return Cell(self.__numcells + other.__numcells)

    def __sub__(self, other):
        if other.__numcells < self.__numcells:
            return Cell(self.__numcells - other.__numcells)
        else:
            raise ValueError("Can't subtract, not enough cells")

    def __mul__(self, other):
        return Cell(self.__numcells * other.__numcells)


    def __truediv__(self, other):
        return Cell(self.__numcells // other.__numcells)

    def make_order(self, row):
        a, b = divmod(self.__numcells, row)
        ret = ''
        for n in range(a):
            ret += '*' * row + '\n'

        if b:
            ret += '*' * b
        else:
            ret = ret.strip()

        return ret



cell = Cell(5)

print(cell)

print(cell + Cell(3))
print(cell * Cell(3))
print(cell - Cell(3))
print(cell / Cell(3))

print(Cell(12).make_order(5))
print('-'*50)
print(Cell(15).make_order(5))



# далее пользуемся pytest
def test_create():
    assert(str(Cell(3)) == 'Cell(3)')


def test_sum():
    assert(Cell(3) + Cell(5) == Cell(8))

def test_sub():
    assert(Cell(5) - Cell(2) == Cell(3))
    with pytest.raises(ValueError) as info:
        Cell(5) - Cell (8)

def test_mul():
    assert(Cell(3) * Cell(4) == Cell(12))

def test_div():
    assert(Cell(8) / Cell(3) == Cell(2))

def test_order():
    assert(Cell(12).make_order(5) == '*****\n*****\n**')
    assert(Cell(15).make_order(5) == '*****\n*****\n*****')