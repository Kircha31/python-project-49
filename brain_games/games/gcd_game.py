from brain_games.ans_que import *
import sys

def gcd():
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
                x = post_response('lose', player, str(answer), str(total))
                sys.exit(x)
        else:
            if answer == total:
                print(post_response('right'))
                count -= 1
            else:
                x = post_response('lose', player, str(answer), str(total))
                sys.exit(x)
    if count == 0:
        print(post_response('win', player))
