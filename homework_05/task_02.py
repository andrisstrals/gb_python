# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

rows = 0
with open('task2.txt') as file:
    for line in file:
        rows += 1
        print(f'Row:{rows:2d} - words:{len(line.split()):2d}')


print(f'Total rows: {rows}')