from brain_games.ans_que import *
import sys

def calc():
    player = welcome_user('calc_game')
    count = 3
    while count > 0:
        numb1 = number()
        numb2 = number()
        symbol = sign()
        answer = que_ans(f'{numb1} {symbol} {numb2}')
        if symbol == '+':
            total = addition(numb1, numb2)
            if total == int(answer):
                print(post_response('right'))
                count -= 1
            else:
                x = post_response('lose', player, answer, str(total))
                sys.exit(x)
        elif symbol == '-':
            total = subtraction(numb1, numb2)
            if total == int(answer):
                print(post_response('right'))
                count -= 1
            else:
                x = post_response('lose', player, answer, str(total))
                sys.exit(x)
        else:
            total = multiplication(numb1, numb2)
            if total == int(answer):
                print(post_response('right'))
                count -= 1
            else:
                x = post_response('lose', player, answer, str(total))
                sys.exit(x)
    
    if count == 0:
        print(post_response('win', player))
