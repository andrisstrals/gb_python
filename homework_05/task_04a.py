# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator

trans = Translator()

with open('task4eng.txt') as filein, open('task4rus_a.txt', 'w') as fileout:
    for line in filein:
        res = trans.translate(line, dest = 'ru')
        print(res.text, file=fileout)
        print(f'{line} --> {res.text}')


