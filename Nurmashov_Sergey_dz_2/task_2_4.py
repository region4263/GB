list_1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in list_1:
    last_whitespace = i.rfind(" ")
    name = i[last_whitespace + 1:].title()
    print(f' Привет, {name}!')
