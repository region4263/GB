for i in range(1, 101):
    if i in [11, 12, 13, 14]:
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    elif 2 <= i % 10 <= 4:
        print(i, 'процента')
    else:
        print(i, 'процентов')