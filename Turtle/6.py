import turtle

turtle.shape("turtle")


def line_for_spider():
    turtle.fd(x)
    turtle.stamp()
    turtle.back(x)

x = 100
y = 18
for i in range(y):
    line_for_spider()
    turtle.rt(360/y)
