import sys
from itertools import zip_longest


user, hobby, result = sys.argv[1:]
if __name__ == '__main__':
    with open(user, 'r', encoding='utf-8') as f_us, \
            open(hobby, 'r', encoding='utf-8') as f_hob:
        user = [i.replace('\n', '') for i in f_us]
        hobby = [j.replace('\n', '') for j in f_hob]

    with open(result, 'w', encoding='utf-8') as f_uh:
        f_uh.writelines(f'{i[0]}: {i[1]}\n' for i in zip_longest(user, hobby, fillvalue=None))
    exit()
