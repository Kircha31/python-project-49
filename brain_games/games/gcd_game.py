from random import randint


RULES = "Find the greatest common divisor of given numbers."


def get_general_divisor_number(numb1, numb2):
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
    numb1, numb2 = randint(0, 100), randint(0, 100)
    total = get_general_divisor_number(numb1, numb2)
    return f"{numb1} {numb2}", str(total)
