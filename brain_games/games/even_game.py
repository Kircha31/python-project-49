from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    numb = number()
    total = 'yes' if numb % 2 == 0 else 'no'
    question = f"Question: {numb}"
    return question, total


def number():
    question = randint(0, 100)
    return question

