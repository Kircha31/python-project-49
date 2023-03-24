from random import randint, choice
import prompt


def number():
    question = randint(0, 100)
    return question


def que_ans(numb):
    answer = prompt.string(f"Question: {numb}\nYour answer: ")
    return answer


def sign():
    signs = ['*', '+', '-']
    return choice(signs)


def multiplication(a, b):
    return a * b


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def post_response(status, player='', answer='', total=''):
    if status == 'lose':
        return f"""'{answer}' is wrong answer ;(. Correct answer was {total}.
Let's try again, {player}!"""
    elif status == 'right':
        return 'Correct!'
    else:
        return f'Congratulations, {player}!'


def calc_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    return name


def even_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    return name


def check(answer):
    correct = ['yes', 'no']
    if answer == correct[0]:
        return True
    elif answer == correct[1]:
        return True
    else:
        return False
