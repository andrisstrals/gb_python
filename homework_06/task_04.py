# Реализуйте базовый класс Car.

# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, *, colour, name, max_speed, is_police = False):
        self.__colour = colour
        self.__name = name
        self.__is_police = is_police
        self.__max_speed = max_speed
        self.__speed = 0
        self.__heading = 0

    def get_coulour(self):
        return self.__colour

    def get_name(self):
        return self.__name

    def get_is_police(self):
        return self.__is_police

    # поскольку подразумеваеться аттрибут скорость, то тут и будем оное задавать как ускорение
    def go(self, acceleration):
        self.__speed += acceleration
        if self.__speed > self.__max_speed:
            self.__speed = self.__max_speed
        print(f'Go. Speed:{self.__speed}')

    # аналогично с ускорением задаем замедление
    def stop(self, deceleration):
        self.__speed -= deceleration
        if self.__speed < 0:
            self.__speed = 0

        print(f'Stopping. Speed:{self.__speed}')


    # раз уж на то пошло, направление сделаем тоже аналоговым, в градусах, на сколько поворачивать
    def turn(self, heading):
        self.__heading += heading
        self.__heading %= 360

        print(f'Turning to:{self.__heading}')

    def show_speed(self):
        return self.__speed

    def show_heading(self):
        return self.__heading




beetle = Car(name = 'VW Beatle', colour='red', max_speed=140)
print(f'Car: {beetle.get_name()}, {beetle.get_coulour()}')
print(f'Is Police: {beetle.get_is_police()}')
print(f'Speed:{beetle.show_speed()}')
print(f'Heading:{beetle.show_heading()}')

beetle.go(20)
assert(beetle.show_speed() == 20)
beetle.go(20)
assert(beetle.show_speed() == 40)
beetle.go(200)
assert(beetle.show_speed() == 140)
beetle.stop(40)
assert(beetle.show_speed() == 100)
beetle.stop(240)
assert(beetle.show_speed() == 0)

beetle.turn(15)
assert(beetle.show_heading() == 15)
beetle.turn(15)
assert(beetle.show_heading() == 30)
beetle.turn(200)
assert(beetle.show_heading() == 230)
beetle.turn(140)
assert(beetle.show_heading() == 10)
beetle.turn(-20)
assert(beetle.show_heading() == 350)


class TownCar(Car):
    speed_limit= 60
    def __init__(self, *, colour, name):
        Car.__init__(self, colour=colour, name=name, max_speed=70)

    def show_speed(self):
        spd = Car.show_speed(self)
        if spd > TownCar.speed_limit:
            print(f'Car {self.get_name()} is speeding!')
        return spd

class WorkCar(Car):
    speed_limit= 40

    def __init__(self, *, colour, name):
        Car.__init__(self, colour=colour, name=name, max_speed=70)

    def show_speed(self):
        spd = Car.show_speed(self)
        if spd > WorkCar.speed_limit:
            print(f'Car {self.get_name()} is speeding!')
        return spd


class SportCar(Car):
    def __init__(self, *, colour, name, max_speed):
        super.__init__(colour=colour, name=name, max_speed=max_speed)

class PoliceCar(Car):
    def __init__(self, *, colour, name, max_speed):
        super.__init__(colour=colour, name=name, max_speed=max_speed, is_police=True)


zaz = TownCar(colour='blue', name='Commuter')
print(f'zaz speed:{zaz.show_speed()}')
zaz.go(50)
assert(zaz.show_speed() == 50)
print(f'zaz speed:{zaz.show_speed()}')
zaz.go(50)
print(f'zaz speed:{zaz.show_speed()}')
assert(zaz.show_speed() == 70)

uaz = WorkCar(colour='yellow', name='Worker')
print(f'uaz speed:{uaz.show_speed()}')
uaz.go(50)
assert(uaz.show_speed() == 50)
print(f'uaz speed:{uaz.show_speed()}')
uaz.go(50)
print(f'uaz speed:{uaz.show_speed()}')
assert(uaz.show_speed() == 70)

# тут, конечно, следует заметить весьма плхой выбор названий методов.
# И вообще переделать в соответсвии с MVC принцыпом. Для начана, в классе Car не должно быть метода show_something.
# Только get_something. По хорошему ныжен отдельный класс типа Dashboard, которий и отображал информацию,
# включая предупреждения о превышении. Но это как бы за рамки.

