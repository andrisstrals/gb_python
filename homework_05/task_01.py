# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('task01.tmp', 'w') as file:
    while True:
        s = input('Enter something or empty line to finish:')
        if not s:
            break
        print(s, file=file)