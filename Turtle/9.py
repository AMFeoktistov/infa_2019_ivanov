import turtle
import math

turtle.shape("turtle")


def polygone(angles, length):
    for i in range(angles):
        turtle.lt(360/angles)
        turtle.fd(length)



angles = 3
R = 20
step = 20
for i in range(50):
    length = 2 * R * math.sin(math.pi / angles)
    turtle.lt((180 - 360/angles)/2)
    polygone(angles, length)
    turtle.rt((180 - 360/angles)/2)
    turtle.penup()
    turtle.fd(step)
    turtle.pendown()
    angles += 1
    R += step
