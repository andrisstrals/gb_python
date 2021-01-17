# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random as rnd
from functools import reduce

filename = 'task5.tmp'
count = 20

with open(filename, 'w') as f:
    for i in range(count):
        f.write(str(rnd.randint(-100, 100)) + ' ')

with open(filename) as f:
    s = f.read()

lst = list(map(int, s.split()))

print(reduce(lambda a, b: a + b, lst))

