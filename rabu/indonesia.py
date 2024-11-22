import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bendera Indonesia")

t = turtle.Turtle()
t.speed(5)

def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

draw_rectangle(-150, 0, 400, 150, "red")

draw_rectangle(-150, -150, 400, 150, "white")

t.hideturtle()
turtle.done()
