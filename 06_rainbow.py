# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1900,1000)
x0=50
y0=50
x1=350
y1=450
step=5
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
for color in rainbow_colors:
    point0 = sd.get_point(x0, y0)
    point1 = sd.get_point(x1, y1)
    sd.line(point0,point1,color=color,width=4)
    y0 = y0 + step
    y1 = y1 + step
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
step=0
for color in rainbow_colors:

    sd.circle(sd.get_point(950,-600),radius=1000-step,color=color,width=20)
    step=step+20


sd.pause()
