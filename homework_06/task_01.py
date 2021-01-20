# Создать класс TrafficLight (светофор).

# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.



#  А что подразумеваеться под продолжительностью? Светофор после запуска сам должен с заданными интервалами переключаться?


import threading
import time


class TrafficLight:
    def __init__(self):
        self.__colour = 'off'
        self.__active = False

    def running(self):
        self.__active = True
        while self.__active:
            if self.__colour == 'red':
                self.__colour = 'orange'
                time2sleep = 2
            elif self.__colour == 'orange':
                self.__colour = 'green'
                time2sleep = 5
            else:
                self.__colour = 'red'
                time2sleep = 7
                
            print(f'Colour: {self.__colour}')
            time.sleep(time2sleep)

    def stop(self):
        self.__active = False


lights = TrafficLight()

th = threading.Thread(target=lights.running)

th.start()

input('Press ENTER to stop')
lights.stop()
th.join()
print('All done. Bye.')
