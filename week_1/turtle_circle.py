import turtle

turtle.setup(width = 1000, height = 1000)
edges = 100
length = 600 / edges
angle = 360 / edges
t = turtle.Pen()
t.pencolor("blue")
t.width(5)
t.speed(100)

for i in range(edges):
    t.forward(length)
    t.right(angle)