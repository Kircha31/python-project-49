from brain_games.games.ans_que import *


def calc():
    player = welcome_user(__file__[58:].strip('.py'))
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
                print(post_response('lose', player, answer, str(total)))
                break
        elif symbol == '-':
            total = subtraction(numb1, numb2)
            if total == int(answer):
                print(post_response('right'))
                count -= 1
            else:
                print(post_response('lose', player, answer, str(total)))
                break
        else:
            total = multiplication(numb1, numb2)
            if total == int(answer):
                print(post_response('right'))
                count -= 1
            else:
                print(post_response('lose', player, answer, str(total)))
                break
    
    if count == 0:
        print(post_response('win', player))
