class QuizIntro:
    def __init__(self, question_count):
        self.question_count = question_count

    def show(self):
        print("****************************")
        print("Welcome to the Quiz Project!")
        print("You will be asked a series of True/False questions.")
        print(f"There are {self.question_count} questions in total.")
        print("Let's get started!\n")