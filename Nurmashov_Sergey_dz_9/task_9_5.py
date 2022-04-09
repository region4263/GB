class Stationery:
    title = "картина"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск письма")


class Pencil(Stationery):
    def draw(self):
        print("Запуск заштриховки")


class Handle(Stationery):
    def draw(self):
        print("Запуск затушевки")


a = Stationery()
a.draw()
b = Pen()
b.draw()
c = Pencil()
c.draw()
d = Handle()
d.draw()
