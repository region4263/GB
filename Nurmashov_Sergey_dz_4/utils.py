from requests import get, utils
from decimal import Decimal


def currency_rates(argv):
    program, *mony = argv
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    print(f'дата - {response.headers.get("Date")}')  # вывод даты вида - Sun, 06 Mar 2022 19:16:30 GMT

    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    mony = ''.join(mony).upper()  # теперь не зависит в каком регистре введён аргумент
    index = content.find(mony)  # ищем индекс первого вхождения значения mony
    if index != -1:  # если искомое значение есть в контенте
        # ищем от этого индекса следующий индекс вхождения значения Value (после которого идет стоимость)
        index_mony = content[index:].find('Value') + 6
        # выбираем подстроку, в которой находится искомое значение стоимости (отводим для этого с запасом 10 символов)
        answer = content[index + index_mony: index + index_mony + 10]
        task = ''
        for i in answer:
            if i.isdigit():
                task += i

        # return float(task) / 10000

        # применение Decimal для приведения стоимости к привычному виду (два знака после запятой)
        dcml = Decimal(task) / 10000
        return dcml.quantize(Decimal("1.00"))


if __name__ == "__main__":
    user = input("введите валюту - ")
    print(f'стоимость - {currency_rates("." + user)}')
