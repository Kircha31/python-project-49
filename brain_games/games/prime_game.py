from brain_games.ans_que import welcome_user, create_full_list, simple_number, que_ans, post_response
from random import choice


def prime():
    global answer, select
    player = welcome_user('prime_game')
    count = 3
    while count > 0:
        list_number = choice(create_full_list())
        select = simple_number(list_number)
        answer = que_ans(list_number)
        if answer not in ['yes', 'no']:
            break
        elif select == answer:
            print(post_response('right'))
            count -= 1
        else:
            break
    if count == 0:
        print(post_response('win', player))
    else:
        print(post_response('lose', player, answer, select))
