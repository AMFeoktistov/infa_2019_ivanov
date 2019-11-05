from graph import *


def treugolnik(x, y, c):  # равносторонний треугольник
    brushColor(c)
    polygon([(x, y), (x + R, y), (x + R / 2, y + (R * 3 ** 0.5 / 2))])


R = 100  # размер стороны квадрата
x = 100  # верхний левый угол
y = 100
treugolnik(x, y, 'red')
x -= R
treugolnik(x, y, 'blue')
x += R / 2
y += R * 3 ** 0.5 / 2
treugolnik(x, y, 'green')

run()
