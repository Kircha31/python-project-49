from random import choice, randint
from brain_games.games import logic


# create list for arifmetik progression
def create_list():
    start = randint(1, 100)
    quantity = randint(5, 10)
    step = randint(1, 10)
    return [x for x in range(start, start + quantity * step, step)]


def select_number(list_str, total):
    list_str[list_str.index(total)] = '..'
    return ' '.join(str(x) for x in list_str)


def is_winner():
    print('What number is missing in the progression?')
    count = 3
    while count > 0:
        list_prog = create_list()
        total = list_prog[choice(range(len(list_prog)))]
        if logic.correct_answer(select_number(list_prog, total), str(total)):
            count -= 1
        else:
            break
    if count == 0:
        return True
    else:
        return False
