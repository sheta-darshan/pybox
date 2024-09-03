from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for que in question_data:
    question = Question(que["text"],que["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
else:
    print("You have completed the quiz")
    print(f"your final score is: {quiz.score}/{quiz.question_number}")

