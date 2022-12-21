from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_txt = question['text']
    answer_txt = question['answer']
    func = Question(question_txt, answer_txt)
    question_bank.append(func)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
