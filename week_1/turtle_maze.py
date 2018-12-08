import turtle

turtle.setup(width = 500, height = 500)
t = turtle.Pen()
t.pencolor("pink")
t.width(2)
t.speed(0)
start_pos = (0, 0)

for i in range(0, 151, 5):
    t.back(i)
    t.right(90)

t.clear()
t.penup()
t.setx(start_pos[0])
t.sety(start_pos[1])
t.pendown()

for i in range(0, 151, 5):
    t.back(i)
    t.right(120)

t.clear()
t.penup()
t.setx(start_pos[0])
t.sety(start_pos[1])
t.pendown()
for i in range(0, 51, 1):
    t.forward(i)
    t.right(36)