import turtle
def Trapesium(ttl, x, y, width, height):
    ttl.penup()
    ttl.goto(x,y)
    ttl.setheading(0)
    ttl.pendown()
    for count in range (2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.penup()

Bob = turtle.Turtle()
Bob.pencolor("red")
Bob.speed(5)
Bob.pensize(3)
Trapesium(Bob, 0, 0, 300, 180,)
turtle.done()