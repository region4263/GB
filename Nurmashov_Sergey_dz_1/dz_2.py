third_power_list = []
total_third_power_list = 0
total_third_power_list_17 = 0

# создаём список кубов
for i in range(1, 1000, 2):
    third_power = i ** 3
    third_power_list.append(third_power)

# задание 2а
# вычисляем сумму цифр каждого числа из списка
for number in third_power_list:
    number = str(number)
    total = 0
    for k in number:
        k = int(k)
        total += k

    # проверяем на кратность 7 и если да, то число в общую сумму
    if total % 7 == 0:
        total_third_power_list += int(number)

print(total_third_power_list)

# задание 2b и 2c (новый список не создавался)
# вычисляем сумму цифр каждого числа из списка
for number in third_power_list:
    number_17 = str(number + 17)
    total = 0
    for k in number_17:
        k = int(k)
        total += k

    # проверяем на кратность 7 и если да, то число в общую сумму
    if total % 7 == 0:
        total_third_power_list_17 += int(number_17)

print(total_third_power_list_17)
