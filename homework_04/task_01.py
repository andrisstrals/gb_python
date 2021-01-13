# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

if len(argv) != 4:
    print('Use: task_01 hours rate bonus')
else:
    _, hours, rate, bonus = argv

    salary = float(hours) * float(rate) + float(bonus)
    print(f'Salary: {salary}')