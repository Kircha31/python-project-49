from brain_games.ans_que import que_ans, post_response
from brain_games.ans_que import welcome_user, create_list
from random import choice


def progressive():
    global answer, total
    player = welcome_user('arfprog_game')
    count = 3
    while count > 0:
        list_prog = create_list()
        total = list_prog[choice(range(len(list_prog)))]
        list_prog[list_prog.index(total)] = '..'
        answer = int(que_ans(' '.join(str(x) for x in list_prog)))
        if total == answer:
            print(post_response('right'))
            count -= 1
        else:
            break

    if count == 0:
        print(post_response('win', player))
    else:
        print(post_response('lose', player, answer, str(total)))
