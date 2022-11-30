# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month =1
total_cost =0
while month <= 10:
    current_expences = expenses * (1.03**(month-1))
    total_cost = total_cost + current_expences

    month = month +1
total_grant = educational_grant *month
deficit = round((total_cost-total_grant),2)
print('Студенту надо попросить',deficit,'руб')
# TODO здесь ваш код
