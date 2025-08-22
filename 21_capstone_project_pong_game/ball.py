from turtle import Turtle

import random

class Ball(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.move_speed = 0.2
        self.x_move = 10
        self.y_move = 10
        

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.2  # reset speed
