class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def show_speed(self):
        print('текущая скорость автомобиля: ', self.speed)

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self):
        print('машина повернула')


class TownCar(Car):
    # свыше 60 km/h
    def show_speed(self):
        print('текущая скорость автомобиля: ', self.speed)
        if self.speed > 60:
            print('превышение скорости на городском автомобиле')


class SportCar(Car):
    def show_speed(self):
        print('текущая скорость автомобиля: ', self.speed)
        if self.speed < 150:
            print('медленно!!!')
        else:
            print('"хорошо летим :)"')


class WorkCar(Car):
    # свыше 40 km/h
    def show_speed(self):
        print('текущая скорость автомобиля: ', self.speed)
        if self.speed > 40:
            print('превышение скорости на рабочем автомобиле')


class PoliceCar(Car):
    def show_speed(self):
        print('текущая скорость автомобиля: ', self.speed)
        print('превышение скорости - это не для нас!')


a = Car(80, "красный", "мерседес", True)
a.show_speed()
print(a.speed)
print(a.color)
print(a.name)
print(a.is_polise)
print()
b = TownCar(72, "синий", "митсубиси", False)
b.show_speed()
print()
c = WorkCar(39, "коричневый", "ЗИЛ", True)
c.show_speed()
print()
d = SportCar(170, "жёлтый", "феррари", True)
print(d.color, d.name)
a.go()
d.show_speed()
a.turn()
a.stop()
print()
e = PoliceCar(87, "синий", "форд", True)
e.show_speed()
