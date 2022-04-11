import os


def path(dir_x, *args):
    dir_path = os.path.join(*args)
    if not os.path.exists(dir_path):
        # если в названии создаваемого объекта нет ".", то создаём папку
        if dir_x.find('.') == -1:
            os.mkdir(dir_path)
        # иначе создаём файл
        else:
            s = open(dir_path, 'w')
            s.close()


with open('config.yaml', encoding='utf-8') as f:
    str_file = f.readlines()
    for item in str_file:
        # "парсим" файл - определяем название объекта и его положение
        # относительно других объектов (т.е. определяем иерархию файлов)
        # по количеству символов слева от названия (переменная "j")
        j = item.find('|--') + 3
        if j == 3:
            main = item[3:-1]
            if not os.path.exists(main):
                os.mkdir(main)
        if j == 6:
            dir_1 = item[6:-1]
            # здесь и в дальнейшем по коду первым аргументом в функцию
            # path передаётся название файла, по которому будет
            # определяться папка это или файл (по наличию точки в названии).
            # остальные аргументы - для создания пути к этому объекту.
            path(dir_1, main, dir_1)
        if j == 9:
            dir_2 = item[9:-1]
            path(dir_2, main, dir_1, dir_2)
        if j == 12:
            dir_3 = item[12:-1]
            path(dir_3, main, dir_1, dir_2, dir_3)
        if j == 15:
            dir_4 = item[15:-1]
            path(dir_4, main, dir_1, dir_2, dir_3, dir_4)
