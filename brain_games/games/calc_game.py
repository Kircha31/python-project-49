from brain_games.ans_que import post_response, subtraction, multiplication, sign
from brain_games.ans_que import welcome_user, number, que_ans, addition


def compare(numb1, numb2, symbol):
    if symbol == '+':
        total = addition(numb1, numb2)
        return total
    elif symbol == '-':
        total = subtraction(numb1, numb2)
        return total
    else:
        total = multiplication(numb1, numb2)
        return total


def calc():
    global answer, total
    player = welcome_user('calc_game')
    count = 3
    while count > 0:
        numb1, numb2, symbol = number(), number(), sign()
        answer = int(que_ans(f'{numb1} {symbol} {numb2}'))
        total = compare(numb1, numb2, symbol)
        if total == answer:
            print(post_response('right'))
            count -= 1
        else:
            break
    if count == 0:
        print(post_response('win', player))
    else:
        print(post_response('lose', player, answer, str(total)))
