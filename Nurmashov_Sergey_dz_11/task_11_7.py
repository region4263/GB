class ComplexNumber:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return ComplexNumber(self.x + other.x)

    def __mul__(self, other):
        return ComplexNumber(self.x * other.x)

    def __str__(self):
        return str(self.x)


a = ComplexNumber(2+5j)
b = ComplexNumber(3+4j)
print(a + b)
print(a * b)
