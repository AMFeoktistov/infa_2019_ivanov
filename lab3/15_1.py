from graph import *


penSize(0)
windowSize(550, 950)
canvasSize(500, 900)
brushColor('midnightblue')
rectangle(0, 0, 500, 90)  # layer1
brushColor('mediumpurple')
rectangle(0, 90, 500, 140)  # layer2
brushColor('plum')
rectangle(0, 140, 500, 220)  # layer3
brushColor('lightpink')
rectangle(0, 220, 500, 340)  # layer4
brushColor('orange')
rectangle(0, 340, 500, 440)  # layer5
brushColor('lightseagreen')
rectangle(0, 440, 500, 900)  # layer6
penSize(5)
penColor('white')
pos = 80, 70
body = 160, 40
wing2 = 240,20
moveTo(pos)

lineTo(body)
lineTo(wing2)




penColor('black')
penSize(1)
x = 20
y = 20
for i in range(900):
    line(x, 20, x, 900)
    line(20, y, 900, y)
    x += 20
    y += 20
run()