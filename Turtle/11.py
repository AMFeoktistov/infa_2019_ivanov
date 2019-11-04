import turtle
import math

turtle.shape('turtle')
turtle.rt(90)

def two_circles():
    for i in range(60):
        turtle.fd(step)
        turtle.rt(6)
    for i in range(60):
        turtle.fd(step)
        turtle.lt(6)

step = 5
for i in range(10):
    two_circles()
    step += 1