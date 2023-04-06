from random import choice


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def simple_number(numb):
    k = 0
    for i in range(2, numb):
        if numb % i == 0:
            k += 1
    if k == 0:
        return 'yes'
    else:
        return 'no'


def get_question_and_right_answer():
    ran_numb = choice([x for x in range(1, 100)])
    correct = simple_number(ran_numb)
    question = f"Question: {ran_numb}"
    return question, correct
