from random import choice
from brain_games.games import logic


def simple_number(numb):
    k = 0
    for i in range(2, numb):
        if numb % i == 0:
            k += 1
    if k == 0:
        return 'yes'
    else:
        return 'no'


def is_winner():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 3
    while count > 0:
        ran_numb = choice([x for x in range(1, 100)])
        correct = simple_number(ran_numb)
        if logic.correct_answer(ran_numb, correct):
            count -= 1
        else:
            break
    if count == 0:
        return True
    else:
        return False
