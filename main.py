from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
QuesionBank=[]
for data in question_data:
    question=Question(data["text"], data["answer"])
    QuesionBank.append(question)
score=0
#print(QuesionBank)
quiz=QuizBrain(QuesionBank)
while quiz.still_has_question():
    score=quiz.next_question()

print(f"\nYou have completed the quiz\nYour final score: {quiz.score}/{len(QuesionBank)}")