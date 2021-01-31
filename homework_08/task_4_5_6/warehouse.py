
from equipmentbase import OfficeEquipment
from myexceptions import ErrorNotAnEqupment

class Warehouse:
    def __init__(self) -> None:
        self.__items = {}
        self.__dispatched = []

    def addItem(self, item, count):

        if not isinstance(item, OfficeEquipment):
            raise ErrorNotAnEqupment(item)

        if item in self.__items:
            self.__items[item] += int(count)
        else:
            self.__items[item] = int(count)

    @property
    def items(self):
        return self.__items

    @property
    def dispatched(self):
        return self.__dispatched

    def num_items(self, what):
        if what in self.__items:
            return self.__items[what]
        else:
            return 0

    def items_by_model(self, what):
        for it in self.__items:
            if it.model == what:
                return it, self.num_items(it)

        return None, 0

    def dispatch(self, model, dest, count):
        item, cnt = self.items_by_model(model)
        if cnt < count:
            raise ValueError(f'No sufficient {model} in warehouse')

        self.__dispatched.append((item, dest, count))
        self.__items[item] -= count
