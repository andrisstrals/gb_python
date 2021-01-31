from equipmentbase import OfficeEquipment

class Copier(OfficeEquipment):
    def __init__(self, *, brand, model, price, weight, ppm):
        super().__init__(brand, model, price, weight)
        self.__ppm = int(ppm)

    @property
    def category(self) -> str:
        return "Copier"

    @property
    def productivity(self):
        return self.__ppm

    def __str__(self) -> str:
        return f'{self.category} {self.brand}, {self.model}, price={self.price}, weight={self.weight}kg, productivity={self.productivity}ppm'

