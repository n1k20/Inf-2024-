from turtle import *  # импорт черепахи

screensize(10000, 10000)
m = 40 # размерность как параметр который можно регулировать
left(90)  # просто переписывается по условию задачи
tracer(0)
speed(100)
right(60)
forward(4 * m)
right(120)
for _ in range(4):
    forward(3 * m)
    right(240)
    forward(3 * m)
    right(120)
forward(4 * m)
right(90)
forward(8 * 3 ** 1 / 2)
right(90)
forward(8 * m)
up()

# проставляем точки для удобства
for x in range(-30, 30):  # сетка с точками
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, 'purple')
done()


"""
задачи на чертежник
"""


left(90)
screensize(10000, 10000)
m = 10
x = 0
y = 0  # координаты начала точки
tracer(0)


def move(a, b):  # формула была конктретно для задачи
    goto(pos()[0] + a * m, pos()[1] + b * m)


for _ in range(3):
    move(15, 37)
    move(-40, -35)
    move(-22, 32)
    move(47, -34)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'green')
done()
"""задачи на перо"""
from turtle import *

left(90)
tracer(0)
screensize(1000, 1000)
m = 40
speed(1000)
penup()
right(30)
forward(4 * m)  # ничего не поменялость с черепахой
right(330)
pendown()
forward(4 * m)
right(90)
forward(7 * m)
right(45)
forward(4 * 2 * 0.5 * m)
right(135)
forward(11 * m)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(5, 'blue')
done()
