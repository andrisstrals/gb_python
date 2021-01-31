from equipmentbase import OfficeEquipment

class Scanner(OfficeEquipment):
    def __init__(self, *, brand, model, price, weight, has_feeder = True):
        super().__init__(brand, model, price, weight)
        self.__has_feeder = bool(has_feeder)

    @property
    def category(self) -> str:
        return "Scanner"

    @property
    def has_feeder(self):
        return self.__has_feeder

    def __str__(self) -> str:
        feed = 'Yes' if self.has_feeder else 'No'
        return f'{self.category} {self.brand}, {self.model}, price={self.price}, weight={self.weight}kg, has feeder:{feed}'

