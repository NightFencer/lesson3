# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1800, 900)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# # TODO здесь ваш код
#
# x_coord = random.randint(100,sd.resolution[0]-100)
# y_coord = random.randint(100,sd.resolution[1]-100)
# point = sd.get_point(x_coord,y_coord)
#
# for r in range(50,61,5):
#     sd.circle(center_position=point,radius=r)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

# def custom_buble(x_coord, y_coord, radius_0, step=3):
#     ''' вывод трех концентрических окружностей с центром x,y,
#         начальным радиусом и шагом приращения радиуса'''
#     point = sd.get_point(x_coord, y_coord)
#     for radiuses in range(radius_0, radius_0 + 1 + step * 3, step):
#         sd.circle(point, radiuses)
#
#
# for i in range(3):
#     x_coord = random.randint(100, sd.resolution[0] - 100)
#     y_coord = random.randint(100, sd.resolution[1] - 100)
#     my_radius = random.randint(10, 200)
#     my_step = 1
#     custom_buble(x_coord, y_coord, my_radius,my_step)
# print(custom_buble.__doc__)


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
# for i in range(1,11):
#     point = sd.get_point(300+i*50, 500)
#     sd.circle(center_position=point,radius=20)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# for x in range(100,1001,100):
#     for y in range(50,151,50):
#         point = sd.get_point(x, y)
#         sd.circle(center_position=point,radius=20)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for i in range(10001):
    point = sd.random_point()
    color_r = random.randint(0,255)
    color_g = random.randint(0,255)
    color_b = random.randint(0,255)
    radius = random.randint(10,100)
    sd.circle(center_position=point,radius=radius,color=[color_r,color_g,color_b],width=3)
print(i)
sd.pause()


