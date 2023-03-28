from brain_games.games.ans_que import *
from random import choice


def prime():
    player = welcome_user('prime_game')
    count = 3
    while count > 0:
        list_number = choice(create_full_list())
        select = simple_number(list_number)
        answer = que_ans(list_number)
        if select == answer:
            print(post_response('right'))
            count -= 1
        else:
            print(post_response('lose', player, answer, select))
            break
    if count == 0:
        print(post_response('win', player))
        