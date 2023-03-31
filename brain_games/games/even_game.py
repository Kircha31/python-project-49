from brain_games.games import logic
from brain_games.ans_que import number


def even_numb(numb):
    return 'yes' if numb % 2 == 0 else 'no'


def is_winner():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 3
    while count > 0:
        question = number()
        total = even_numb(question)
        if logic.correct_answer(question, total):
            count -= 1
        else:
            break
    if count == 0:
        return True
    else:
        return False
