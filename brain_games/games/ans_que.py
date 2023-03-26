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


def welcome_user(game):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    if game == 'calc_game':
        print('What is the result of the expression?')
    elif game == 'even_game':
        print('Answer "yes" if the number is even, otherwise answer "no"')
    else:
        print("Find the greatest common divisor of given numbers.")
    return name


def check(answer):
    correct = ['yes', 'no']
    if answer == correct[0]:
        return True
    elif answer == correct[1]:
        return True
    else:
        return False


def check_zero(numb1, numb2):
    if numb1 == 0:
        return numb2
    else:
        return numb1


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
