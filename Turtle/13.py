import turtle

turtle.shape('turtle')


def circle():
    for i in range(60):
        turtle.fd(step)
        turtle.rt(6)


def face():
    turtle.begin_fill()
    turtle.color('black', 'yellow')
    circle()
    turtle.end_fill()


def eye():
    turtle.begin_fill()
    turtle.color('black', 'blue')
    circle()
    turtle.end_fill()


def nose():
    turtle.color('brown')
    turtle.width(5)
    turtle.fd(10)



def mouth():
    turtle.color('red')
    turtle.width(5)
    for i in range(30):
        turtle.fd(step)
        turtle.lt(6)


step = 10
face()
turtle.penup()
turtle.rt(90)
turtle.fd(70)
turtle.rt(90)
turtle.fd(40)
turtle.pendown()
step /= 10
eye()
turtle.penup()
turtle.back(80)
turtle.pendown()
eye()
turtle.penup()
turtle.fd(40)
turtle.lt(90)
turtle.fd(30)
turtle.pendown()
nose()
turtle.penup()
turtle.rt(90)
turtle.fd(50)
turtle.lt(90)
turtle.fd(20)
turtle.pendown()
step *= 5
mouth()
turtle.done()
