# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_div(a, b):
    return a / b if b != 0 else None

def test_task_1():
    nums = list(map(float, input('Task 1. Eneter two numbers separated by space: ').split()))
    if len(nums) != 2:
        print('Error: two numbers required.')
        return
    print(f'{nums[0]} / {nums[1]} = {my_div(nums[0], nums[1])}')


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#    имя, фамилия, год рождения, город проживания, email, телефон.
#    Функция должна принимать параметры как именованные аргументы.
#    Реализовать вывод данных о пользователе одной строкой.

# Тут непонятно, то ли вывод написать одной строчкой, то ли печатать в одну строку...

def print_user1(*, first_name = None, last_name = None, year_of_birth = None,
             city = None, email = None, phone = None):
    print(f'User: {first_name} {last_name} YOB: {year_of_birth}, {city}, {email}, {phone}')


def print_user2(**kwargs):
    required = ['first_name', 'last_name', 'year_of_birth', 'city', 'email', 'phone']
    for r in required:
        if not r in kwargs:
            print(f'Parameter {r} required.')
            return
    print('User:', end=' ')
    for k in kwargs:
        print(f'{k}:{kwargs[k]}', end=' ')
    print()

def test_task_2():
    print_user1(first_name = 'Robby', last_name = 'Garret', year_of_birth = 1978,
                city = 'Norfolk', email = 'rg@some.com', phone = '+447812345678')
    print_user2() #expected error
    print_user2(first_name = 'Robby', last_name = 'Garret', year_of_birth = 1978,
                city = 'Norfolk', email = 'rg@some.com', phone = '+447812345678')

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#    и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    return a + b + c - min(a, b, c)

def test_task_3():
    assert my_func(1, 2, 3) == 5
    assert my_func(2, 3, 1) == 5
    assert my_func(3, 1, 2) == 5
    print('All pass')

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
#    Необходимо выполнить возведение числа x в степень y.
#    Задание необходимо реализовать в виде функции my_func(x, y).
#    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#    Подсказка: попробуйте решить задачу двумя способами.
#    Первый — возведение в степень с помощью оператора **.
#    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_pow1(x, y):
    return x ** y

def my_pow2(x, y):
    res = 1
    for i in range(0, abs(y)):
        res *= x
    return res if y > 0 else 1/res

def test_task_4():
    assert my_pow1(2, -2) == 0.25
    assert my_pow1(2, 2) == 4
    assert my_pow2(2, -2) == 0.25
    assert my_pow2(2, 2) == 4
    print('All pass')

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#    При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
#    разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
#    уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
#    программы завершается. Если специальный символ введен после нескольких чисел, то вначале
#    нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def int_func():
    total = 0
    while True:
        lst = input('Enter few numbers separated by spaces: ').strip().split()
        for n in lst:
            if n.isdigit():
                total += int(n)
            else:
                print(f'Total: {total}')
                return
        print(f'Total: {total}')


def test_task_5():
    int_func()


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#    но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
#    Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
#    но каждое слово должно начинаться с заглавной буквы.
#    Необходимо использовать написанную ранее функцию int_func().

# в принципе встроенний метод title() по моему удовлетворяет требования
def str_func(text):
    return text.title()

# изобретаем велосипед :D
def str_func1(text):
    if len(text):
        text = list(text)
        text[0] = text[0].upper()
        text = ''.join(text)
    return text

def test_sentence(sentence):
    lst = sentence.split()
    for i, w in enumerate(lst):
        lst[i] = str_func1(w)
    return ' '.join(lst)

def test_task_6():
    assert str_func('abcd') == 'Abcd'
    assert str_func1('abcd') == 'Abcd'
    assert str_func('hello world') == 'Hello World'
    assert test_sentence('hello world') == 'Hello World'
    print(str_func('hello world'))
    print(test_sentence('hello world'))




if __name__ == '__main__':
    while True:
        task = input('Select task to test (1 - 6) or Q to quit: ')
        if task.upper() == 'Q':
            break
        elif task == '1':
            test_task_1()
        elif task == '2':
            test_task_2()
        elif task == '3':
            test_task_3()
        elif task == '4':
            test_task_4()
        elif task == '5':
            test_task_5()
        elif task == '6':
            test_task_6()
        else:
            print('Try again...')
