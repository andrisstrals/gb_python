# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


from printer import Printer
from scanner import Scanner
from copier import Copier
from warehouse import Warehouse
from myexceptions import ErrorNotAnEqupment


w = Warehouse()

w.addItem(Printer(brand= 'Canon', model= 'MG1600', price= 165.0, weight= 5), 5)
w.addItem(Printer(brand= 'HP', model= 'some', price= 12.0, weight= 4.5), 8)

w.addItem(Scanner(brand='HP', model='Scanjet 3500', price=380, weight=4.8, has_feeder = False), 7)
w.addItem(Copier(brand='Brother', model='MFCL3750CDW', price=299.99, weight=15, ppm=36), 3)

print(w.items)

print(w.items_by_model(3))
print(w.items_by_model('some'))

w.dispatch('Scanjet 3500', 'office', 3)
print(w.items_by_model('Scanjet 3500'))