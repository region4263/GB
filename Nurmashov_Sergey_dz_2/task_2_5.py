price_list = [37.5, 58.39, 27.09, 99.0, 69.83, 33.79, 37.74, 86.29, 74.96, 24.62]
# A
for i in price_list:
    x = str(i).split(".")
    if len(x[1]) == 1:
        x[1] += "0"
    print(f'{x[0]} руб {x[1]} коп', end=", ")
print("id - ", id(price_list))
# B
price_list.sort()
for i in price_list:
    x = str(i).split(".")
    if len(x[1]) == 1:
        x[1] += "0"
    print(f'{x[0]} руб {x[1]} коп', end=", ")
print("id - ", id(price_list))  # id не изменился, объект тот же
# C
price_list_2 = price_list[::-1]
for i in price_list_2:
    x = str(i).split(".")
    if len(x[1]) == 1:
        x[1] += "0"
    print(f'{x[0]} руб {x[1]} коп', end=", ")
print("id - ", id(price_list_2))  # id изменился, создан новый список

# D
for i in price_list[-5:]:
    x = str(i).split(".")
    if len(x[1]) == 1:
        x[1] += "0"
    print(f'{x[0]} руб {x[1]} коп', end=", ")
