from equipmentbase import OfficeEquipment

class Printer(OfficeEquipment):
    def __init__(self, *, brand, model, price, weight, iscolour = True):
        super().__init__(brand, model, price, weight)
        self.__iscolour = bool(iscolour)

    @property
    def category(self) -> str:
        return "Printer"

    @property
    def iscolour(self):
        return self.__iscolour

    def __str__(self) -> str:
        c = 'Yes' if self.iscolour else 'No'
        return f'{self.category} {self.brand}, {self.model}, price={self.price}, weight={self.weight}kg, colour:{c}'

