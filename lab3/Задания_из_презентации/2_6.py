from graph import *


def triangle(koords,c):
    brushColor(c)
    polygon(koords)
    circle(x, y, R)


R = 10
koords = [(100, 200), (145, 200), (70, 130)]
x, y = 68, 128
triangle(koords, 'blue')
koords = [(190, 200), (145, 200), (220, 130)]
x, y = 222, 128
triangle(koords, 'green')
koords = [(130, 200), (160, 200), (145, 120)]
x, y = 145, 118
triangle(koords, 'red')

run()