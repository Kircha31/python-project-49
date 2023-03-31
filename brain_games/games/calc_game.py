import operator
from brain_games.ans_que import number
from brain_games.games import logic
from random import choice


action = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def is_winner():
    print('What is the result of the expression?')
    count = 3
    while count > 0:
        numb1, numb2, = number(), number()
        symbol = choice(['*', '+', '-'])
        total = str(action[symbol](numb1, numb2))
        if logic.correct_answer(f'{numb1}{symbol}{numb2}', total):
            count -= 1
        else:
            break
    if count == 0:
        return True
    else:
        return False
