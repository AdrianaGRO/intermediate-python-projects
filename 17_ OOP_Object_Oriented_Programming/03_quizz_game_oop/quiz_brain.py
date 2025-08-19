# This class is responsible for managing the quiz logic.


class QuizBrain:
    """This class manages the quiz logic, including tracking the current question, score, and checking answers."""
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # Check if there are still questions left
    def still_has_questions(self):
       return self.question_number < len(self.question_list)

    # Move to the next question and check the user's answer
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False)? \n")
        self.check_answer(user_answer, current_question.answer)

    # Check the user's answer against the correct answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
        print("\n")

