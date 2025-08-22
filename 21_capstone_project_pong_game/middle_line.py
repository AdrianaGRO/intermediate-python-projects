from turtle import Turtle

class MiddleLine(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.setheading(270)

    def draw_line(self):
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)