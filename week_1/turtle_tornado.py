import turtle

t = turtle.Pen()

t.color('red')
t.speed(0)
angle = 91

for x in range(1000):
    t.forward(x)
    t.left(angle)

t.hideturtle();