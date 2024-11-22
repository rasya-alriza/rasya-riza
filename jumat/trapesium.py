import turtle
def Trapesium(ttl, x, y, width, height, botWidth, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.setheading(45)
    ttl.color(color)
    ttl.begin_fill()

    for count in range (2):
        ttl.forward(width)
        ttl.right(45)
    for count in range (1):
        ttl.forward(height)
        ttl.right(135)
    for count in range(1):
        ttl.forward(botWidth)
    ttl.end_fill()


Bob = turtle.Turtle()
Bob.pencolor("green")
Bob.speed(5)
Bob.pensize(3)
Trapesium(Bob, -130, 0, 180, 180,440, "green")
turtle.done()