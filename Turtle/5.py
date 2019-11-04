import turtle


def circle_for_turtle():
    for i in range(4):
        turtle.fd(x)
        turtle.rt(90)


turtle.shape("classic")
x = 40
for i in range(10):
    circle_for_turtle()
    turtle.lt(135)
    turtle.penup()
    turtle.fd((20**2*2)**0.5)
    turtle.pendown()
    turtle.rt(135)
    x += 40
