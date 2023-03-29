from brain_games.ans_que import *
from random import choice
import sys


def prime():
    player = welcome_user('prime_game')
    count = 3
    while count > 0:
        list_number = choice(create_full_list())
        select = simple_number(list_number)
        answer = que_ans(list_number)
        if not check(answer):
            x = post_response('lose', player, answer, 'yes/no')
            sys.exit(x)
        elif select == answer:
            print(post_response('right'))
            count -= 1
        else:
            x = post_response('lose', player, answer, select)
            sys.exit(x)
    if count == 0:
        x = post_response('win', player)
        sys.exit(x)
        