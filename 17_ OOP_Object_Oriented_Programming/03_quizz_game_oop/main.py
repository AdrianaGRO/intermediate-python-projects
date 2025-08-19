

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from quizz_intro import QuizIntro

# Initialize the question bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# Initialize the quiz intro and show it
quiz_intro = QuizIntro(len(question_bank))
quiz_intro.show()

# Initialize the quiz brain and start the first question
quiz = QuizBrain(question_bank)
quiz.next_question()

# Loop through the quiz until all questions are answered
while quiz.question_number < len(quiz.question_list):
    quiz.next_question()

# End the quiz and show the final score
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")