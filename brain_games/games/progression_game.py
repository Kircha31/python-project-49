from random import choice, randint


RULES = 'What number is missing in the progression?'


# create list for arifmetik progression
def create_list():
    start = randint(1, 100)
    quantity = randint(5, 10)
    step = randint(1, 10)
    return [x for x in range(start, start + quantity * step, step)]


def select_number(list_str, total):
    list_str[list_str.index(total)] = '..'
    return ' '.join(str(x) for x in list_str)


def get_question_and_right_answer():
    list_prog = create_list()
    total = list_prog[choice(range(len(list_prog)))]
    return select_number(list_prog, total), str(total)
