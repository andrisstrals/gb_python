# Реализовать класс Stationery (канцелярская принадлежность).

# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def draw(self):
        print('Stationery draw called')


class Pen(Stationery):
    def draw(self):
        print('Pen draw called')


class Pencil(Stationery):
    def draw(self):
        print('Pencil draw called')


class Handle(Stationery): #вообще-то Highlighter. Хотя может на американском Handle, не уверен.
    def draw(self):
        print('Handle draw called')


st = Stationery()
pen = Pen()
pencil = Pencil()
highlighter = Handle()


st.draw()
pen.draw()
pencil.draw()
highlighter.draw()



