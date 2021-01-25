# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#    размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы:
#     для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod

class Clothing(ABC):

    def __init__(self, *, size):
        self.sz = size

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    def size(self):
        return self.sz

    @size.setter
    def size(self, sz):
        self.sz = sz

    @abstractmethod
    def calculate_fabric(self):
        pass

    @property
    def fabric(self):
        return self.calculate_fabric()


class Coat(Clothing):
    def __init__(self, *, size):
        super().__init__(size=size)

    @property
    def name(self):
        return "Coat"

    def calculate_fabric(self):
        return self.size/6.5 + 0.5


class Suit(Clothing):
    def __init__(self, *, size):
        super().__init__(size=size)

    @property
    def name(self):
        return "Suit"

    def calculate_fabric(self):
        return 2 * self.size + 0.3


# тут не разу не понимаю, какие размеры, и в каких единицах ткань должна получиться
coat = Coat(size = 48)
print(f'{coat.name} of size {coat.size} needs {coat.fabric:0.2f} m of fabric')
coat.size = 100
print(f'{coat.name} of size {coat.size} needs {coat.fabric:0.2f} m of fabric')


suit = Suit(size = 178)
print(f'{suit.name} of size {suit.size} needs {suit.fabric:0.2f} cm of fabric')
suit.size = 186
print(f'{suit.name} of size {suit.size} needs {suit.fabric:0.2f} cm of fabric')

