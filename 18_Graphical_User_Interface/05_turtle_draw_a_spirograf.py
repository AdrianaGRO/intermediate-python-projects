#How to draw a spirograph

from turtle import Turtle, Screen
import turtle
import random




screen = Screen()
screen.bgcolor("white")
screen.title("Spirograph with Turtle")

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

t = Turtle()
t.speed("fastest")







for _ in range(36):
    t.color(random_color())
    t.circle(150)
    t.right(10)





screen.exitonclick()