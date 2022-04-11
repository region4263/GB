import os


def path(main, *args):
    if not os.path.exists(main):
        os.mkdir(main)
    os.chdir(main)
    for i in args:
        if not os.path.exists(i):
            os.mkdir(i)


path('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')

# =========================================
#
# для ручного ввода названия папок
#
# main_dir = input('введите название основной папки: ')
# dir_in_main = input('введите названия вложенных папок через запятую: ').replace(' ', '').split(',')
# path(main_dir, *dir_in_main)
