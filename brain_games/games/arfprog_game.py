from brain_games.games.ans_que import *


def progressive():
    player = welcome_user(__file__[58:].strip('.py'))
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
            print(post_response('lose', player, answer, str(total)))
            break

    if count == 0:
        print(post_response('win', player))
