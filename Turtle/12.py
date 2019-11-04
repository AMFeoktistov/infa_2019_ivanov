import turtle

turtle.shape('turtle')
turtle.penup()
turtle.back(450)
turtle.pendown()
turtle.lt(90)


def arc(step):
    for i in range(90):
        turtle.fd(step)
        turtle.rt(2)

step = 1
for i in range (20):
    arc(step)
    step /= 10
    arc(step)
    step *= 10