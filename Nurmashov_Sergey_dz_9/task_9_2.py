class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self):
        mas = int(input('введите массу асфальта:  '))
        thic = int(input('введите число см толщины полотна:  '))
        total = self._length * self._width * mas * thic / 1000
        print(f'{total} т')


a = Road(5000, 20)
a.massa()
