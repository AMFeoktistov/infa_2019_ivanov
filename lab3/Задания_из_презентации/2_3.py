from graph import *


def treugolnik(x, y, c):
    brushColor(c)
    polygon([(x, y), (x, y-50), (x+70, y-50)])
x = y = 100
treugolnik(x, y, 'red')
x -= 70
y += 50
treugolnik(x, y, 'blue')
x = 100
treugolnik(x, y, 'green')
run()