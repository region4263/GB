class Worker:
    name = 'Serzh'
    surname = 'Nuare'
    position = 'boss'
    _income = {"wage": 100, "bonus": 2000}


class Position(Worker):
    # полное имя сотрудника
    def get_gull_name(self):
        name_sur = Worker.name + " " + Worker.surname
        print("полное имя сотрудника: ", name_sur)

    # доход с учётом премии
    def get_total_income(self):
        income = 0
        for val in Worker._income.values():
            income = income + val
        print("доход с учётом премии: ", income)


a = Position()
print(f'имя: {a.name}')
print(f'фамилия: {a.surname}')
print(f'должность: {a.position}')
print(f'доход: {a._income}')
a.get_gull_name()
a.get_total_income()