from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    the_question = item['question']
    correct_answer = item['correct_answer']
    question_objs = Question(the_question, correct_answer)
    question_bank.append(question_objs)


quiz = QuizBrain(question_bank)

while quiz.continue_questions():
    quiz.question_process()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

