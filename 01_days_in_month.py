# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца (1-12): ")
monthes =[(1,3,5,7,8,10,12),(4,6,9,10),(2)]
monthes_names =['январе','фервале','марте','апреле','мае','июне','июле','августе','сентябре','октябре','ноябре','декабре']
try:
    month = int(user_input)
    if month in monthes[0]:
        print('В', monthes_names [month-1], '31 день')
    elif month in monthes[1]:
        print('В', monthes_names [month-1], '30 дней')
    elif month == 2:
        print('В', monthes_names [month-1], '28 дней')
    else:
        print('некоректный номер месяца')
    print('Вы ввели', month)

except:
    print('Это не номер, а ерунда')




# TODO здесь ваш код
