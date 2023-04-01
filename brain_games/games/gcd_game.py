from brain_games.ans_que import number
from brain_games.games import logic


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


def is_winner():
    print("Find the greatest common divisor of given numbers.")
    count = 3
    while count > 0:
        a, b = number(), number()
        total = gcd_number(a, b)
        if logic.correct_answer(f'{a} {b}', str(total)):
            count -= 1
        else:
            break
    if count == 0:
        return True
    else:
        return False
