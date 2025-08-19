# How do draw different shapes with turtle
# Drawing a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen
import random

colors = [
    "red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime", "gold", "brown",
      "black", "gray", "navy", "turquoise", "cornflowerblue", "royalblue", "deepskyblue", "dodgerblue", "skyblue",
        "steelblue", "lightblue"
]
t = Turtle()
t.shape("circle")

# List of number of sides for each shape
shapes = [3, 4, 5, 6, 7, 8, 9, 10]

for num_sides in shapes:
    t.color(random.choice(colors))
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

screen = Screen()
screen.exitonclick()