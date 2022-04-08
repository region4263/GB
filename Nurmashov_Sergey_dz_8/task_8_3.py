def type_logger(func):
    f_name = str(func).split()[1]  # получаем название функции -> calc_cube

    def ty(*args):
        for i in args:
            g = f'{f_name}({i}: {type(i)})'
            yield g

    return ty


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5, 7.54)
print(*a, sep=', ')
