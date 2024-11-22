import turtle
screen = turtle.Screen()
screen.title("Monitor")

def Layar(ttl, x, y, width, height):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for count in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.penup()

def kaki(ttl, x, y, width, height):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for count in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.penup()

def kaki2(ttl, x, y, width,miring ,  height):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(-2)
    ttl.pendown()
    for count in range(1):
        ttl.forward(width)
        ttl.right(45)
        ttl.forward(miring)
        ttl.right(90)
        ttl.forward(miring)
        ttl.right(55)
        ttl.forward(50)
        ttl.left(45)
        ttl.forward(height)
        ttl.right(45)
        ttl.forward(miring)
        ttl.right(90)
        ttl.forward(miring)
        ttl.right(55)
        ttl.forward(33)

t = turtle.Turtle()
t.pencolor("blue")
t.speed(7)
t.pensize(3)

Layar(t, -50, 50, 300, 100)
kaki(t, 95, -50, 20, 50)
kaki2(t,95, -100, 60, 15, 30)
t.hideturtle()
turtle.done()
