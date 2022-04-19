class Warehouse:
    # приём оргтехники на склад
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.gx = {}
        self.gy = {}
        self.gz = {}

    def __str__(self):
        return f'на складе находится: Printer - {self.x},Scanner - {self.y}, Copier - {self.z}'

    # передача в подразделения
    def give(self):
        _g, _t, _u = Warehouse.of_give(self.x)
        self.x = {_g: _t}  # осталось
        self.gx = {_g: _u}  # передали
        _g, _t, _u = Warehouse.of_give(self.y)
        self.y = {_g: _t}  # осталось
        self.gy = {_g: _u}  # передали
        _g, _t, _u = Warehouse.of_give(self.z)
        self.z = {_g: _t}  # осталось
        self.gz = {_g: _u}  # передали
        print(f'передали в подразделение: Printer - {self.gx},Scanner - {self.gy}, Copier - {self.gz}')
        print(f'на складе осталось: Printer - {self.x},Scanner - {self.y}, Copier - {self.z}')

    @staticmethod
    def of_give(off):
        for key, val in off.items():
            print(f"всего на складе {off}. сколько передать '{key}' в подразделение компании? ", end='')
            us = Warehouse.valid_num()
            if us > val:
                print(f"на складе имеется только {val} '{key}', передаём всё")
                val = 0
                return key, val, us
            else:
                val -= us
                return key, val, us

    # валидация количества переданной оргтехники
    @staticmethod
    def valid_num():
        while True:
            try:
                num = int(input('введите число: '))
            except ValueError:
                print("введено не число")
            else:
                break
        return num


class Office:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Printer(Office):
    def __init__(self, a, b, d):
        super().__init__(a, b)
        self.d = d

    def give(self):
        print('сколько передать на склад Printer? ', end='')
        return {self.a: Warehouse.valid_num()}


class Scanner(Office):
    def __init__(self, a, b, e):
        super().__init__(a, b)
        self.e = e

    def give(self):
        print('сколько передать на склад Scanner? ', end='')
        return {self.a: Warehouse.valid_num()}


class Copier(Office):
    def __init__(self, a, b, f):
        super().__init__(a, b)
        self.f = f

    def give(self):
        print('сколько передать на склад Copier? ', end='')
        return {self.a: Warehouse.valid_num()}


p = Printer("hp", 5, "синий")
s = Scanner("canon", 3, "черный")
c = Copier("xerox", 2, "серый")
k = Warehouse(p.give(), s.give(), c.give())
k.give()
