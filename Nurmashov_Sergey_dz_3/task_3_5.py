from random import choice


def get_jokes(word_1, word_2, word_3, iter):
    """Создание необходимого количества шуток"""
    for _ in range(iter):
        print(f'"{choice(word_1)} {choice(word_2)} {choice(word_3)}"')


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

user_iter = int(input("введите количество выводимых шуток:  "))
get_jokes(nouns, adverbs, adjectives, user_iter)
