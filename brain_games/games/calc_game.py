from brain_games.ans_que import *


def calc():
    global answer, total
    player = welcome_user('calc_game')
    count = 3
    while count > 0:
        numb1, numb2, symbol = number(), number(), sign()
        answer = que_ans(f'{numb1} {symbol} {numb2}')
        if symbol == '+':
            total = addition(numb1, numb2)
            if total == int(answer):
                print(post_response('right'))
                count -= 1
            else:
                break
        elif symbol == '-':
            total = subtraction(numb1, numb2)
            if total == int(answer):
                print(post_response('right'))
                count -= 1
            else:
                break
        else:
            total = multiplication(numb1, numb2)
            if total == int(answer):
                print(post_response('right'))
                count -= 1
            else:
                break
    if count == 0:
        print(post_response('win', player))
    else:
        print(post_response('lose', player, answer, str(total)))
