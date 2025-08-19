# How to draw a dashed line with turtle graphics

from turtle import Turtle, Screen

t = Turtle()

for _ in range(10): 
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

screen = Screen()
screen.exitonclick()