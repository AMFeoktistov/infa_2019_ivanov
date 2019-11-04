import turtle

turtle.shape("turtle")

x = 0.1
y = 5
for i in range(2000):
    turtle.fd(x)
    turtle.lt(y)
    x += 0.01
