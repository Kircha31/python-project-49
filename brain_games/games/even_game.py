from brain_games.ans_que import *
import sys, os


def even():
    player = welcome_user('even_game')
    count = 3
    while count > 0:
        question = number()
        answer = que_ans(question)
        if answer not in ['yes', 'no']:
            quit(post_response('lose', player, answer, 'yes/no'))
        elif question % 2 == 0:
            if check(answer):
                print(post_response('right'))
                count -= 1
            else:
                sys.exit(post_response('lose', player, answer, 'no'))
        else:
            if not check(answer):
                print(post_response('right'))
                count -= 1
            else:
                sys.exit(post_response('lose', player, answer, 'yes'))
    
    if count == 0:
        print(post_response('win', player))
        sys.exit(os.EX_OK)
        
