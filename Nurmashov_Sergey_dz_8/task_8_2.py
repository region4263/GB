import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for i in f:
        # вариант №1 - поиск pv4/pv6, применив одно регулярное выражение
        remote_addr = re.search('(\w{,4}[:]){4,}\w+|(\d{1,3}.){3}\d{1,3}', i).group()  # pv4/pv6

        # вариант №2 - поиск pv4/pv6 по отдельности
        # pv6 = re.search('(\w{,4}[:]){4,}\w+', i)
        # if pv6:
        #     remote_addr = pv6.group()
        # else:
        #     remote_addr = re.search('(\d{1,3}.){3}\d{1,3}', i).group()  # pv4

        request_datetime = re.search('\d\S+\s\S\d+', i).group()  # 17/May/2015:08:05:49 +0000
        request_type = re.search('[A-Z]{3,4}\s', i).group()  # GET
        requested_resource = re.search('\S\w{9}\S+\d', i).group()  # /downloads/product_2
        response_code = re.search('\s\d+\s', i).group().strip()  # 404
        response_size = re.search('\s\d+\s\d+', i).group().split(' ')[2]  # 334
        total = remote_addr, request_datetime, request_type, requested_resource, response_code, response_size
        print(total)
