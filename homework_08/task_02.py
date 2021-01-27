# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class ErrorDivByZero(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"Don't even think of dividing {self.num} by ZERO!"

def divide(a, b):
    if not b:
        raise ErrorDivByZero(a)

    return a / b



while True:
    s = input('Enter two numbers or emty line to finish: ')
    if not s:
        break

    try:
        nums = list(map(int, s.split()))
        print(f'{nums[0]} / {nums[1]} = {divide(nums[0], nums[1])}')
    except ErrorDivByZero as e:
        print(f'ERROR: {e}')
    except Exception as e:
        print(f'Something went wrong: {e}')

