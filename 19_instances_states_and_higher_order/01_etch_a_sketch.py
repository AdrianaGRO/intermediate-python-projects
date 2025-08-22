from turtle import Turtle, Screen, teleport

t = Turtle()
t.color("white")
screen = Screen()
screen.title("Etch A Sketch")
screen.setup(width=600, height=600)
screen.bgcolor("black")


def move_forward():
    t.forward(10)

def counter_clockwise():
    t.left(10)

def clockwise():
    t.right(10)

def move_backward():
    t.backward(10)

def circle():
    t.circle(80)

def semicircle():
    t.circle(80, 180)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()



    
screen.listen()
screen.onkey(move_forward, key = "w")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(move_backward, "s")
screen.onkey(clear_screen, "c")
screen.onkey(circle, "o")
screen.onkey(semicircle, "p")


screen.exitonclick()
