# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from collections import Counter

initial = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
cnt = Counter(initial)
res = [el for el in initial if cnt.get(el) == 1]
print(res)

# можно и так, если некуда спешить :)
cnt1 = dict((i, initial.count(i)) for i in initial)
res1 = [el for el in initial if cnt1.get(el) == 1]
print(res1)

# С dict и count получаеться complexity O(n**2)
# а Counter более умный, вот мой тест, quick'n'dirty:

# from random import randint
# import time

# testlist = [randint(0, 1000) for el in range(1000)]

# start = time.time()
# for i in range(1000):
#     Counter(testlist)
# elapsed_counter = time.time() - start

# start = time.time()
# for i in range(1000):
#     dict((i, testlist.count(i)) for i in testlist)
# elaplsed_dict = time.time() - start

# print(f'time:\n  Counter:{elapsed_counter}\n     dict:{elaplsed_dict}')

# у меня получилось:
# time:
#   Counter:0.04501152038574219
#      dict:10.422810316085815
