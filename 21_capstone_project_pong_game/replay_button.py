
from turtle import Turtle, Screen

class ReplayButton(Turtle):
    def __init__(self, x=0, y=-200, width=120, height=50, label="Replay"):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.hideturtle()
        self.penup()
        self.visible = False  # Button should not be visible initially
    
    def draw_button(self):  
        if not self.visible:
            return
        
        self.clear()  # Clear any previous drawing
        # Position the turtle to draw a centered rectangle
        self.goto(self.x - self.width / 2, self.y + self.height / 2)
        self.pendown()
        self.color("white", "gray")  # Set fill color
        self.begin_fill()
        for _ in range(2):
            self.forward(self.width)
            self.right(90)
            self.forward(self.height)
            self.right(90)
        self.end_fill()
        self.penup()
        
        # Write the label in the center of the button
        self.goto(self.x, self.y)
        self.color("black")
        self.write(self.label, align="center", font=("Arial", 16, "normal"))
    
    def show(self):
        """Show the button after game ends"""
        self.visible = True
        self.draw_button()
    
    def hide(self):
        """Hide the button during gameplay"""
        self.visible = False
        self.clear()

    def is_click_on_button(self, x, y):
        if not self.visible:
            return False
        if self.x - self.width / 2 < x < self.x + self.width / 2 and self.y - self.height / 2 < y < self.y + self.height / 2:
            return True
        return False
