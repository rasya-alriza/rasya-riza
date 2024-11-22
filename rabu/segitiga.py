import turtle
def Trapesium(ttl, x, y, width, height):
    ttl.penup()
    ttl.goto(x,y)
    ttl.setheading(45)
    ttl.pendown()
    for count in range (2):
        ttl.forward(width)
        ttl.right(90)
    for count in range (1):
        ttl.right(45)
        ttl.forward(height)
    ttl.penup()

Bob = turtle.Turtle()
Bob.pencolor("yellow")
Bob.speed(5)
Bob.pensize(3)
Trapesium(Bob, -50, 0, 300, 430,)
turtle.done()