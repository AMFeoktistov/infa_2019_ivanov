from graph import *


def treugolnik(x, y, c):
    brushColor(c)
    polygon([(x, y), (x + R/2, y + (3**0.5*R/2) - z), (x - R/2,y + (3**0.5*R/2) - z)])


x = 300
y = 200
R = 100
z = 50
brushColor("brown")
rectangle(x - R/10, y + (3**0.5*R/2) - z, x + R/10, y + (3**0.5*R/2) - z + R/5)
for i in range(6):
    treugolnik(x, y, 'green')
    y -= 15
    R -= R/6
    z -= 50/6
run()