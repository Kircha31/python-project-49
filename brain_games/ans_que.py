from random import randint, choice
from typing import List

import prompt


# generate random number
def number():
    question = randint(0, 100)
    return question


# Question formation and receiving answer
def que_ans(numb):
    answer = prompt.string(f"Question: {numb}\nYour answer: ")
    return answer


# Random math sign
def sign():
    signs = ['*', '+', '-']
    return choice(signs)


# multiplication
def multiplication(a, b):
    return a * b


# addition
def addition(a, b):
    return a + b


# subtraction
def subtraction(a, b):
    return a - b


# Formation answer on the action user
def post_response(status, player='', answer='', total=''):
    if status == 'lose':
        return f"""'{answer}' is wrong answer ;(. Correct answer was {total}.
Let's try again, {player}!"""
    elif status == 'right':
        return 'Correct!'
    else:
        return f'Congratulations, {player}!'


# Greet users
def welcome_user(game):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    if game == 'calc_game':
        print('What is the result of the expression?')
    elif game == 'even_game':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'prime_game':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif game == 'arfprog_game':
        print('What number is missing in the progression?')
    else:
        print("Find the greatest common divisor of given numbers.")
    return name


# Check corretly answer
def check(answer):
    correct = ['yes', 'no']
    if answer == correct[0]:
        return True
    elif answer == correct[1]:
        return True
    else:
        return False


# Check is it number of zero
def check_zero(numb1, numb2):
    if numb1 == 0:
        return numb2
    else:
        return numb1


# Find max divisor number
def gcd_number(numb1, numb2):
    total = []
    if numb1 > numb2:
        temp = numb2
    else:
        temp = numb1
    for i in range(1, temp + 1):
        if numb1 % i == 0 and numb2 % i == 0:
            total.append(i)
    return max(total)


# create list for arifmetik progression
def create_list():
    start = randint(1, 100)
    quantity = randint(5, 10)
    step = randint(1, 10)
    arf_prog = [x for x in range(start, start + quantity * step, step)]
    return arf_prog


# Check is it number simple
def simple_number(numb):
    k = 0
    for i in range(2, numb):
        if numb % i == 0:
            k += 1
    if k == 0:
        return 'yes'
    else:
        return 'no'


# create list
def create_full_list():
    return [x for x in range(1, 100)]
