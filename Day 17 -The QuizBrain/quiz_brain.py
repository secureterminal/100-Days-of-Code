class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.q_list = question_list

    def still_has_questions(self):
        if self.question_number < len(self.q_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.q_list[self.question_number]

        self.question_number += 1
        choice = input(f'Q.{self.question_number}: {current_question.text} (True/False)?: ')
        # print(f'choice: {choice} answer: {current_question.answer}')

        # print(self.question_number, len(self.q_list))

        if choice.lower() == current_question.answer.lower():
            self.score += 1
            print('You got it right!')
            print(f'The correct answer was {current_question.answer}')
            print(f'Your current score is {self.score}/{self.question_number}')
            return True
        else:
            # self.score += 1
            print('You got it wrong!')
            print(f'The correct answer is {current_question.answer}')
            print(f'Your current score is {self.score}/{self.question_number}')
            return False






