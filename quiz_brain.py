class QuizBrain:
    def __init__(self, question_list):
        self.question_list=question_list
        self.question_number=0
        self.score=0

    def still_has_question(self):
        q_Num = self.question_number
        if q_Num<len(self.question_list):
            return True
        else:
            return False



    def next_question(self):

        q_Num = self.question_number
        current_question=self.question_list[q_Num]
        q_Num += 1
        user_ans=input(f"\nQ{q_Num}: {current_question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(current_question, user_ans)

    def check_answer(self, current_question, user_ans):
        if current_question.answer.lower()==user_ans.lower():
            print("You got it right")
            self.score+=1
        else:
            print("That's Wrong")
        print(f"The correct answer was: {current_question.answer} ")
        print(f"Current Score: {self.score}/{self.question_number}")
