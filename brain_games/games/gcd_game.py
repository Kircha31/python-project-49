from brain_games.ans_que import *


def gcd():
    global answer, total
    player = welcome_user(__file__[58:].strip('.py'))
    count = 3
    while count > 0:
        a, b = number(), number()
        answer = int(que_ans(f'{a} {b}'))
        total = gcd_number(a, b)
        if a == 0 or b == 0:
            if answer == a or answer == b:
                print(post_response('right'))
                count -= 1
            else:
                break
        else:
            if answer == total:
                print(post_response('right'))
                count -= 1
            else:
                break
    if count == 0:
        print(post_response('win', player))
    else:
        print(post_response('lose', player, str(answer), str(total)))
        
