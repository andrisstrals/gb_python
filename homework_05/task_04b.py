# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

mydict = {
'One' : 'Один',
'Two' : 'Два',
'Three' : 'Три',
'Four' : 'Четыре',
'Five' : 'Пять',
'Six' : 'Шесть',
'Seven' : 'Семь',
'Eight' : 'Восемь',
'Nine' : 'Девять',
'Ten' : 'Десять',
'Eleven' : 'Одиннадцать',
'Twelve' : 'Двенадцать'
}

with open('task4eng.txt') as filein, open('task4rus_b.txt', 'w') as fileout:
    for line in filein:
        spl = line.split()
        res = []
        for it in spl:
            if mydict.get(it):
                res.append(mydict.get(it))
            else:
                res.append(it)

        fileout.write(' '.join(res) + '\n')


