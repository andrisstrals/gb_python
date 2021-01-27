# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

from datetime import date
import pytest

class Date:

    datestring = ''

    def __init__(self, datestring):
        Date.datestring = datestring


    # а под типом "число" подразумеваеться datetime.date?
    @classmethod
    def extractDate(cls):
        nums = list(map(int, cls.datestring.split('-')))
        assert(len(nums) == 3)
        return date(nums[2], nums[1], nums[0])

    @staticmethod
    def verify(*, year, month, day):
        try:
            date(year, month, day)
            return True
        except Exception as ex:
            print(f'Bad values {ex}')
            return False



d = Date('9-5-1945')
print(d.extractDate())

print(Date.verify(year=2000, month=2, day=29))
print(Date.verify(year=2001, month=2, day=29))


# далее пользуемся pytest
def test_extract():
    assert(Date('9-5-1945').extractDate() == date(1945, 5, 9))

def test_bad_extract():
    with pytest.raises(ValueError) as err:
        Date('13, 13, 13').extractDate()

    with pytest.raises(AssertionError) as err:
        Date('131313').extractDate()


def test_verify():
    assert(Date.verify(year=2000, month=2, day=29))
    assert(not Date.verify(year=2001, month=2, day=29))
    assert(not Date.verify(year=2001, month=22, day=22))

