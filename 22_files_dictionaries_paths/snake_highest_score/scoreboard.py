from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roboto", 18, 'bold')





class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("22_files_dictionaries_paths/snake_highest_score/data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score(self.score)

    def update_score(self, score):
        self.clear()
        self.write(arg=f"Score: {score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("22_files_dictionaries_paths/snake_highest_score/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score(self.score)

    def increase_score(self):
        self.score += 1
        self.update_score(self.score)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write(arg=f"Final Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        