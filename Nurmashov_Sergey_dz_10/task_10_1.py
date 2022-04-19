import random


class Matrix:
    def __init__(self, num_1, num_2, num_3, num_4):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = num_3
        self.num_4 = num_4
        self.mtrx = [
            [self.num_1, self.num_2],
            [self.num_3, self.num_4]
        ]

    def __str__(self):
        self.c = []
        for i in self.mtrx:
            self.c.append('  '.join(map(str, i)))
        return '\n'.join(self.c)

    def __add__(self, other):
        return Matrix(self.num_1 + other.num_1, self.num_2 + other.num_2,
                      self.num_3 + other.num_3, self.num_4 + other.num_4)


mtrx_1 = Matrix(random.randint(10, 49), random.randint(10, 49),
                random.randint(10, 49), random.randint(10, 49))
mtrx_2 = Matrix(random.randint(10, 49), random.randint(10, 49),
                random.randint(10, 49), random.randint(10, 49))
print(mtrx_1)
print(mtrx_2)
print(mtrx_1 + mtrx_2)
