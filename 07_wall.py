# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1800, 900)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
x0 = y0 = 0
# x1=350
# y1=450
step_x = 100
step_y = 50
row = 0

# TODO здесь ваш код\

for y0 in range(0, 901, step_y):
    if row / 2 == row // 2:
        shear = 50
    else:
        shear = 0
    for x0 in range(0 - shear, 1801, step_x):
        point_list = [sd.get_point(0 + x0, 0 + y0), sd.get_point(100 + x0, 0 + y0), sd.get_point(100 + x0, 50 + y0),
                      sd.get_point(0 + x0, 50 + y0)]
        sd.lines(point_list=point_list, width=4, color=sd.COLOR_ORANGE)
    row = row + 1

sd.pause()
