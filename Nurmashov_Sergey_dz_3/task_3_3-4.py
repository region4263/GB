def thesaurus(names):
    val_name = []  # список для создания значений val в словаре
    d = {}  # словарь для формирования готового ответа
    names.sort()
    for i in names:
        # если имени ещё нет в списке значений
        if i not in val_name:
            # отбираем в списке names имена, начинающиеся на первую букву выбранного имени
            val_name = list(filter(lambda x: x.startswith(i[0]), names))
            d.update({i[0]: val_name})
    print(d)


names_list = ['Иван', 'Мария', 'Петр', 'Илья', 'Николай']
thesaurus(names_list)