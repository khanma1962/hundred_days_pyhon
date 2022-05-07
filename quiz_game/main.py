from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain

question_bank = [] # list of question objects

for question in question_data:
    # print(question)
    question_text = question['text']
    question_answer = question['answer']
    q_class = Question(text=question_text, answer=question_answer)
    question_bank.append(q_class)

quiz = QuizBrain(question_bank)
# quiz.next_question()

# still_on = True
while (quiz.still_has_qustions()):
    quiz.next_question()

print("You have completed the quiz.")
print(f"You final score is {quiz.score} / {self.question_number}")
