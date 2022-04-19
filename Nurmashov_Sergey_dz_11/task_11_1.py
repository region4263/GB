class Date:
    def __init__(self, ls):
        self.ls = ls

    @classmethod
    def int_date(cls, ls):
        return cls([int(i) for i in ls[0].split('-')])

    @staticmethod
    def valid_date(ls):
        a = [int(i) for i in ls[0].split('-')]
        if not 1 <= a[0] <= 31:
            print("не правильный день")
        elif not 1 <= a[1] <= 12:
            print("не правильный месяц")
        elif not 1922 <= a[2] <= 2022:
            print("не правильный год")
        else:
            print("дата правильная")


x = ['12-09-2022']
a = Date.int_date(x)
print(a.ls)
Date.valid_date(x)

y = ['132-09-2022']
a = Date.int_date(y)
print(a.ls)
Date.valid_date(y)
