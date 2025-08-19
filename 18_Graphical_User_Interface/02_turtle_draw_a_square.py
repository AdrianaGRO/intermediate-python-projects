from turtle import Turtle, Screen
import random


colors = ["red", "green", "blue", "yellow", "purple", "orange"]

t = Turtle()
t.shape("circle")
t.color(random.choice(colors))

#drawing a square

for _ in range(4):
    t.forward(100)
    t.right(90)


screen = Screen ()
screen.exitonclick()