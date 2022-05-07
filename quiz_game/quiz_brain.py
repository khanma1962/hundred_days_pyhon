

class QuizBrain():

    def __init__(self, question_bank):
        self.score = 0
        # self.total = 0
        self.question_number = 0
        self.question_list = question_bank

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        user_input = input(f"Q.{self.question_number}: \"{ current_question}\"(true/false)? ")
        
        self.question_number += 1
        self.check_answer(user_input, current_answer)
        
        return 

    def check_answer(self,user_input, current_answer):
        if user_input.lower() == current_answer.lower():
            self.score += 1
            print(f"You are right!!! Your score is {self.score}/{self.question_number}")

        else:
            print("Sorry, you are wrong!!!")
            print(f"The correct answer is {current_answer}!!! You score is {self.score}/{self.question_number}")
        print("\n")

    def still_has_qustions(self):
        # still_on = input("Do you want to play (y/n)? ").lower()
        still_on = 'y'
        # print(type(still_on))
        # print(still_on)
        return still_on == 'y' and self.question_number < len(self.question_list )



