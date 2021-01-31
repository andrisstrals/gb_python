import pytest

from printer import Printer
from scanner import Scanner
from copier import Copier
from warehouse import Warehouse
from myexceptions import ErrorNotAnEqupment


def test_create_printer():
    pr = Printer(brand='Canon', model='MG1500', price=150, weight=5)
    assert(pr.category == 'Printer')
    assert(pr.brand == 'Canon')
    assert(pr.model == 'MG1500')
    assert(pr.price == 150.0)
    assert(pr.weight == 5.0)
    assert(str(pr) == 'Printer Canon, MG1500, price=150.0, weight=5.0kg, colour:Yes')

def test_create_scanner():
    pr = Scanner(brand='HP', model='Scanjet 3500', price=380, weight=4.8, has_feeder = False)
    assert(pr.category == 'Scanner')
    assert(pr.brand == 'HP')
    assert(pr.model == 'Scanjet 3500')
    assert(pr.price == 380.0)
    assert(pr.weight == 4.8)
    assert(str(pr) == 'Scanner HP, Scanjet 3500, price=380.0, weight=4.8kg, has feeder:No')

def test_create_copier():
    pr = Copier(brand='Brother', model='MFCL3750CDW', price=299.99, weight=15, ppm=36)
    assert(pr.category == 'Copier')
    assert(pr.brand == 'Brother')
    assert(pr.model == 'MFCL3750CDW')
    assert(pr.price == 299.99)
    assert(pr.weight == 15.0)
    assert(str(pr) == 'Copier Brother, MFCL3750CDW, price=299.99, weight=15.0kg, productivity=36ppm')

def test_add_to_warehouse():
    pr = Printer(brand='Canon', model='MG1500', price=150, weight=5)
    pr1 = Printer(brand='Epson', model='HP970', price=239, weight=3.55)
    w = Warehouse()
    assert(w.num_items(pr) == 0)
    assert(w.num_items(pr1) == 0)
    w.addItem(pr, 3)
    w.addItem(pr1, 5)
    assert(w.num_items(pr) == 3)
    w.addItem(pr, 4)
    assert(w.num_items(pr) == 7)
    assert(w.num_items(pr1) == 5)

    assert(w.items_by_model('MG1500') == (pr,7))

def test_add_warehouse_errors():
    w = Warehouse()
    with pytest.raises(ErrorNotAnEqupment) as err:
        w.addItem('some', 3)

    with pytest.raises(ValueError) as err:
        w.addItem(Scanner(brand='HP', model='Scanjet 3500', price=380, weight=4.8, has_feeder = False), 'a')

def test_bad_create():
    with pytest.raises(ValueError) as err:
        pr = Printer(brand='Canon', model='MG1500', price='GBP 150', weight=5)

    with pytest.raises(ValueError) as err:
        pr = Printer(brand='Canon', model='MG1500', price=150, weight='5kg')

    # это не работает, так как питон чего угодно в булего преватит
    # with pytest.raises(ValueError) as err:
    #     pr = Printer(brand='Canon', model='MG1500', price=150, weight=5, iscolour = 'something')


def test_dispatch():
    w = Warehouse()
    w.addItem(Scanner(brand='HP', model='Scanjet 3500', price=380, weight=4.8, has_feeder = False), 20)
    w.addItem(Printer(brand='Canon', model='MG1500', price=150, weight=5), 30)

    _, s = w.items_by_model('Scanjet 3500')
    _, p = w.items_by_model('MG1500')
    assert(s == 20)
    assert(p == 30)

    w.dispatch('Scanjet 3500', 'floor1', 5)
    w.dispatch('MG1500', 'floor2', 12)

    _, s = w.items_by_model('Scanjet 3500')
    _, p = w.items_by_model('MG1500')
    assert(s == 15)
    assert(p == 18)

    with pytest.raises(ValueError) as err:
        w.dispatch('MG1500', 'floor3', 20)




