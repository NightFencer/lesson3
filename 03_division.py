# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
multiplier = 1
while b * multiplier <= a:
    multiplier = multiplier+1
multiplier = multiplier -1
print('Целоцисленное деление',a,'на',b,'дает',multiplier)

print(a//b)
# TODO здесь ваш код
