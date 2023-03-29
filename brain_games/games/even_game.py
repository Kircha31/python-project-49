from brain_games.ans_que import *
import sys


def even():
    player = welcome_user('even_game')
    count = 3
    while count > 0:
        question = number()
        answer = que_ans(question)
        if answer not in ['yes', 'no']:
            x = post_response('lose', player, answer, 'yes/no')
            sys.exit(x)
        elif question % 2 == 0:
            if check(answer):
           
                print(post_response('right'))
                count -= 1
            else:
                x = post_response('lose', player, answer, 'no')
                sys.exit(x)
        else:
            if check(answer):
                print(post_response('right'))
                count -= 1
            else:
                x = post_response('lose', player, answer, 'yes')
                sys.exit(x)
    
    if count == 0:
        x = post_response('win', player)
        sys.exit(x)
