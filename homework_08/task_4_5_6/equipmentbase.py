
from abc import ABC, abstractmethod, abstractproperty



class OfficeEquipment(ABC):
    """
        Defines abstract base class for office equipment items
    """
    def __init__(self, brand, model, price, weight):
        self.__brand = str(brand)
        self.__model = str(model)
        self.__price = float(price)
        self.__weight = float(weight)

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        return self.__str__()

    @abstractproperty
    def category(self) -> str:
        pass

    @property
    def brand(self):
            return self.__brand

    @property
    def model(self):
            return self.__model

    @property
    def price(self):
            return self.__price

    @property
    def weight(self):
        return self.__weight
