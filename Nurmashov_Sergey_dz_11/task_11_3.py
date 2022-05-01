class Zero(ValueError):
    def __init__(self, mes):
        self.mes = mes

    def __str__(self):
        return f"{self.mes} - введено не число!"


ls = []
while True:
    num = input('введи число (если вводить больше не надо, напиши слово "stop") - ')
    if num == 'stop':
        break
    try:
        num = int(num)
    except ValueError:
        print(f'{Zero("проблема")}')
    else:
        ls.append(num)
print(ls)
