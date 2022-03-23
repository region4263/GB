src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result_1 = set()
tmp = []
for i in src:
    if i not in tmp:
        result_1.add(i)
    else:
        result_1.discard(i)
    tmp.append(i)
result = [el for el in src if el in result_1]
print(result)
