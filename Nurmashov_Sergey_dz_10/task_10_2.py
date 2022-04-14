class Clothes:

    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def coat(self):
        a = self.v/6.5 + 0.5
        return a

    @property
    def suit(self):
        b = 2*self.h + 0.3
        return b


c = Clothes(52, 5)
print(c.coat)
print(c.suit)
