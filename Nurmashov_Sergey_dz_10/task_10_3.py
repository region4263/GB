class Cell:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Cell(self.x + other.x)

    def __sub__(self, other):
        if self.x > other.x:
            return Cell(self.x - other.x)
        else:
            return "разность количества ячеек двух клеток меньше нуля"

    def __mul__(self, other):
        return Cell(self.x * other.x)

    def __floordiv__(self, other):
        return Cell(self.x // other.x)

    def __str__(self):
        return str(self.x)

    def make_order(self, r):
        while self.x > r:
            print('*' * r + '\\n', end='')
            self.x -= r
        print('*' * self.x)


a = Cell(17)
b = Cell(16)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
Cell.make_order(b, 6)
