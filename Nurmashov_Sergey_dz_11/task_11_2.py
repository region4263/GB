class Zero(ZeroDivisionError):
    def __init__(self, mes):
        self.mes = mes

    def __str__(self):
        return f"{self.mes} - ZeroDivisionError"


try:
    100 / int(input('введи число - '))
except ZeroDivisionError:
    print(f'{Zero("problem")}')
finally:
    print('продолжаем работу')
