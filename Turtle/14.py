import turtle

turtle.shape('turtle')


length = 200
angles = 11
for i in range(angles):
    turtle.fd(length)
    turtle.lt(180-180/angles)