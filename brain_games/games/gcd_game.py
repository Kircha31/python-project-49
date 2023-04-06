from random import randint


RULES = "Find the greatest common divisor of given numbers."


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


def get_question_and_right_answer():
    numb1, numb2 = number(), number()
    total = gcd_number(numb1, numb2)
    question = f"Question: {numb1} {numb2}"
    return question, str(total)


def number():
    question = randint(0, 100)
    return question
