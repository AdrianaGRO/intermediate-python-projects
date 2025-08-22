from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, 'bold')
SCORE_LEFT_POSITION = (-140, 250)
SCORE_RIGHT_POSITION = (140, 250)


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()


class GameOverBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
    
    def display_winner(self, winner):
        self.goto(0, 0)
        self.write(arg=f"{winner} Wins!", move=False, align=ALIGNMENT, font=FONT)