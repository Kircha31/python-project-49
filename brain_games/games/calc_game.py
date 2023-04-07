import operator
from random import choice, randint


RULES = 'What is the result of the expression?'

action = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_question_and_right_answer():
    numb1, numb2, = randint(0, 100), randint(0, 100)
    symbol = choice(['*', '+', '-'])
    total = str(action[symbol](numb1, numb2))
    return f"{numb1} {symbol} {numb2}", total
