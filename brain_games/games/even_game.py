from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    numb = randint(0, 100)
    total = 'yes' if numb % 2 == 0 else 'no'
    return numb, total
