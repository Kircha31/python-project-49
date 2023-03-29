from brain_games.ans_que import *
import sys


def even():
    player = welcome_user('even_game')
    count = 3
    while count > 0:
        question = number()
        answer = que_ans(question)
        if answer not in ['yes', 'no']:
            print(post_response('lose', player, answer, 'yes/no'))
            return False
        elif question % 2 == 0:
            if check(answer):
                print(post_response('right'))
                count -= 1
            else:
                print(post_response('lose', player, answer, 'no'))
                return False
        else:
            if check(answer):
                print(post_response('right'))
                count -= 1
            else:
                print(post_response('lose', player, answer, 'yes'))
                return False
    
    if count == 0:
        print(post_response('win', player))
        return True
