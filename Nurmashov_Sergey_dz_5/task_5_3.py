tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['1А', '2В', '3Б', '4В', '5Б', '6Б', '7В', '8Б', '4В', '5Б', '6Б', '7В', '8Б']

# Заполняем список classes значениями None, если он меньше списка tutors.
while len(tutors) > len(classes):
    classes.append(None)

x = ((tutors[i], classes[i]) for i in range(len(tutors)))
print(type(x), *x)
