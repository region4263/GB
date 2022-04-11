import os

files_dic = {}
pth = os.getcwd()
for root, _, files in os.walk(pth):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.stat(file_path).st_size
        if file_size < 10:
            size = 10
        elif 100 > file_size > 10:
            size = 100
        elif 1000 > file_size > 100:
            size = 1000
        elif 10000 > file_size > 1000:
            size = 10000
        else:
            size = 100000
        # создаём словарь с ключом "size" и значением - список файлов
        files_dic[size] = files_dic.get(size, []) + [file]

d = {}
for key, val in sorted(files_dic.items()):
    val = len(val)
    d[key] = val
print(d)
