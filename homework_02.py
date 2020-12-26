# 1. Создать список и заполнить его элементами различных типов данных.
#    Реализовать скрипт проверки типа данных каждого элемента.
#    Использовать функцию type() для проверки типа.
#    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

separ = '\n' + '-' * 50 + '\n'

mylist = [1, ['text', 55], True, 'превет', 4.12, {'a', 'b', 38}, {'name' : 'andy', 'age' : 57}, ('a', 76)]

for elem in mylist:
    print(f'елемент: {elem}, тип: {type(elem)}' )

print(separ)

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
#    элементы с индексами 0 и 1, 2 и 3 и т.д.
#    При нечетном количестве элементов последний сохранить на своем месте.
#    Для заполнения списка элементов необходимо использовать функцию input().

mylist = []
while True:
    action = input('Ваше действие:\n\t1.Добавить елемент\n\t2.Закончить и перемешать: ')
    if action == '1':
        elem = input('Добавте елемент: ')
        if elem.isdigit():
            elem = int(elem)
        mylist.append(elem)
    elif action == '2':
        break
    else:
        print('Плохой выбор...')

l = len(mylist) & 0xfffe  # игнорируем нечётный елемент
for idx in range(0, l, 2):
    mylist[idx], mylist[idx + 1] = mylist[idx + 1], mylist[idx]

print(mylist)

print(separ)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#    Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#    Напишите решения через list и через dict.

while True:
    month = input('Введите номер месяца (1-12): ')
    if month.isdigit() and 1 <= int(month) <= 12:
        month = int(month)
        break
    else:
        print('Вы уверены? Попробуйте ещё.')

monthnames = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

# вариант #1 list
seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето',
           'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f'{monthnames[month - 1]} - это {seasons[month - 1]}.')

# вариант #2 dict
seasons = {1 : 'зима', 2 : 'зима', 3 : 'весна', 4 : 'весна',
           5 : 'весна', 6 : 'лето', 7 : 'лето', 8 : 'лето',
           9 : 'осень', 10 : 'осень', 11 : 'осень', 12 : 'зима'}
print(f'{monthnames[month - 1]} - это {seasons[month]}.')

# вариант #3 dict
seasons = { 'зима' : [12, 1, 2], 'весна' : [3, 4, 5],
            'лето' : [6, 7, 8], 'осень' : [9, 10, 11] }
for s, m in seasons.items():
    if month in m:
        print(f'{monthnames[month - 1]} - это {s}.')
        break


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
#    Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
#    Если в слово длинное, выводить только первые 10 букв в слове.



# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#    У пользователя необходимо запрашивать новый элемент рейтинга.
#    Если в рейтинге существуют элементы с одинаковыми значениями,
#    то новый элемент с тем же значением должен разместиться после них.

#    Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#    Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#    Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#    Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#    Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].



# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

