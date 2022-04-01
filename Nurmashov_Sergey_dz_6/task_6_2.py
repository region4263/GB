with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    remout_addr = [i[: i.find('-') - 1] for i in f]
    max_x = 0
    ip = ''
    for i in set(remout_addr):
        x = remout_addr.count(i)
        if x > max_x:
            max_x = x
            ip = i

    print(f'IP адрес спамера: {ip} \nколичество отправленных им запросов: {max_x}')  # 216.46.173.126  2350
