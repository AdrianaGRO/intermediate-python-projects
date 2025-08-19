# This class represents a single question in the quiz.
# It contains the question text and the correct answer.

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

