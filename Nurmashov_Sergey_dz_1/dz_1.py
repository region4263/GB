duration = int(input('введите количество секунд:  '))

seconds = duration % 60
minutes = duration % 3600 // 60
hours = duration % 86400 // 3600
days = duration // 86400

if duration < 60:
    print(f'{duration}')
elif duration < 3600:
    print(f'{minutes} мин {seconds} сек')
elif duration < 86400:
    print(f'{hours} час {minutes} мин {seconds} сек')
else:
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')