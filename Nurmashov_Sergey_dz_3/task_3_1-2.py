def num_trunslate_adv(eng):
    words_dic = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                 'nine': 'девять', 'ten': 'десять'}
    # если начинается с большой буквы
    if eng.istitle():
        # преобразуем в маленькую букву и смотрим в словаре
        if words_dic.get(eng.lower()):
            # если есть, то возвращаем значение с большой буквы
            return words_dic.get(eng.lower()).title()
    else:
        return words_dic.get(eng)


en_word = input('введи слово на английском от 1 до 10:  ')
print(num_trunslate_adv(en_word))
