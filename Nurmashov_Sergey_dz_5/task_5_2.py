user_num = int(input('введите предел диаппазона:  '))
odd_num = (i for i in range(1, user_num + 1, 2))
print(*odd_num)
