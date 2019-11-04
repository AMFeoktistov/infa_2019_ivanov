import turtle

turtle.shape('turtle')

def two_circles():
    for i in range(2):
        for i in range(60):
            turtle.fd(5)
            turtle.rt(6)
        turtle.rt(180)

n = 3

for i in range(n):
    two_circles()
    turtle.rt(360/(2*n))
