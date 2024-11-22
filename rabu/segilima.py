import turtle
def Trapesium(ttl, x, y, width, height):
    ttl.penup()
    ttl.goto(x,y)
    ttl.setheading(45)
    ttl.pendown()
    for count in range (5):
        ttl.forward(width)
        ttl.right(72)
    ttl.penup()

Bob = turtle.Turtle()
Bob.pencolor("purple")
Bob.speed(5)
Bob.pensize(3)
Trapesium(Bob, -50, 0, 100, 430,)
turtle.done()