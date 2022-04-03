import os
import shutil


def path(dir_x, *args):
    dir_path = os.path.join(*args)
    if not os.path.exists(dir_path):
        if dir_x.find('.') == -1:
            os.mkdir(dir_path)
        else:
            s = open(dir_path, 'w')
            s.close()


with open('config.yaml', encoding='utf-8') as f:
    str_file = f.readlines()
    for item in str_file:
        j = item.find('|--') + 3
        if j == 3:
            main = item[3:-1]
            if not os.path.exists(main):
                os.mkdir(main)
        if j == 6:
            dir_1 = item[6:-1]
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

# до этого момента всё одно и то же, что и в ДЗ "task_7_2"
# ===========================================

# создаём дополнительную папку 'templates', в которую будем
# собирать шаблоны "html" со всего проекта
os.chdir(main)
if not os.path.exists('templates'):
    os.mkdir('templates')

# сменяем текущую директорию на 'templates' и начинаем сканировать
# весь проект
pth = os.getcwd()
os.chdir('templates')
for root, _, files in os.walk(pth):
    for i in files:
        if i.endswith('.html'):
            # если шаблон найден, то определяем название родительской
            # папки "dir_1" и путь к папке 'dir_2", в которой находится
            # родительская папка
            dir_2, dir_1 = os.path.split(root)
            if not os.path.exists(dir_1):
                os.mkdir(dir_1)
            # проверяем где был найден шаблон:
            # если найден не в той же папке "templates", в которую мы и
            # собираем шаблоны, то производим копирование
            if os.getcwd() != dir_2:
                shutil.copytree(root, dir_1, dirs_exist_ok=True)
