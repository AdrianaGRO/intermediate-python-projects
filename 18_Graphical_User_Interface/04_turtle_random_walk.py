# Random Walk

from turtle import Turtle, Screen
import random
import turtle

screen = Screen()
screen.bgcolor("grey")
screen.title("Random Walk with Turtle")
t = Turtle()
turtle.colormode(255)  # Set the color mode to RGB

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]
t.speed("fastest")
t.pensize(10)
t.shape("arrow")

for _ in range(500):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))




screen.update()  # Update the screen to show the drawn path
screen.delay(0)  # Set the delay to 0 for instant drawing
screen.mainloop()