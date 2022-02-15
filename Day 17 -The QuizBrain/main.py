from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

# for question in question_bank:
    # print('Text: ', question.text)
    # print('Answer: ', question.answer)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quizzer = quiz.next_question()
    print('\n')


