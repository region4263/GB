def val_checker(lam):
    def wrap_1(func):
        def wrap_2(arg):
            if lam(arg):
                total = func(arg)
                return total
            else:
                raise ValueError(f"wrong val {arg}")

        return wrap_2

    return wrap_1


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(-5)
print(a)
