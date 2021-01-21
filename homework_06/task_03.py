# Реализовать базовый класс Worker (работник).

# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров.


class Worker:
    def __init__(self, *, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income



class Position(Worker):
    def __init__(self, *, name, surname, position, income):
        Worker.__init__(self, name=name, surname=surname, position=position, income=income)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']




mike = Position(name = "Mike", surname="Hogg", position="Teamlead", income={"wage":10000, "bonus":5000})



print(f'name     {mike.name}')
print(f'surname  {mike.surname}')
print(f'position {mike.position}')
print(f'income   {mike._income}')

print(f'Full name:     {mike.get_full_name()}')
print(f'Total Income:  {mike.get_total_income()}')
