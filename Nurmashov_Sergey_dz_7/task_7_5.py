import os
import  json

pth = os.getcwd()
file_ls = {}
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
        # создаём словарь с ключом "size" и значением - список с
        # расширениями файлов
        i = file.find('.')
        file_ls[size] = file_ls.get(size, []) + [file[i + 1:]]  # {10000: ['py', 'py', 'py']}

files_dic = {}
for key, val_1 in sorted(file_ls.items()):
    total = len(val_1)
    val_1 = list(set(val_1))
    files_dic[key] = total, val_1
print(files_dic)

with open('my_project_summary.json', 'w', encoding='utf-8') as f:
    json.dump(files_dic, f)
