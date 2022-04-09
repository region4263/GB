import time


class TrafficLight:
    __color = 'красный', 'желтый', 'зеленый'

    def running(self, gr):
        while True:
            for i in TrafficLight._TrafficLight__color:
                print(i)
                if i == 'красный':
                    time.sleep(7)
                elif i == 'желтый':
                    time.sleep(2)
                else:
                    time.sleep(gr)


a = TrafficLight()
green = int(input('введите продолжительность состояния (зелёный):  '))
a.running(green)
