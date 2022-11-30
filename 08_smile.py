# -*- coding: utf-8 -*-
import random

# (определение функций)
import simple_draw as sd
sd.resolution =(1800,1000)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
# TODO здесь ваш код


def smiling_circle(x0, y0, color):
    point_list = [sd.get_point(-20 + x0, 0 + y0), sd.get_point(-10 + x0, -15 + y0), sd.get_point(10 + x0, -15 + y0),
                  sd.get_point(20 + x0, 0 + y0)]
    sd.lines(point_list=point_list, width=2, color=color)
    sd.circle(center_position=sd.get_point(x0, y0), color=color, radius=25)
    sd.circle(center_position=sd.get_point(x0 - 10, y0 + 10), color=color, radius=5)
    sd.circle(center_position=sd.get_point(x0 + 10, y0 + 10), color=color, radius=5)
    sd.circle(center_position=sd.get_point(x0, y0), color=color, radius=2)



for i in range(1111):
    x = random.randint(50, 1750)
    y = random.randint(50, 950)
    c = random.randint(0, 6)
    col = rainbow_colors[c]
    smiling_circle (x, y, col)

sd.pause()