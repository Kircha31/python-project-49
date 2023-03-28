from brain_games.ans_que import *


def even():
    player = welcome_user('even_game')
    count = 3
    while count > 0:
        question = number()
        answer = que_ans(question)
        if not answer in ['yes', 'no']:
            print(post_response('lose', player, answer, 'yes/no'))
            break
        elif question % 2 == 0:
            if check(answer):
                print(post_response('right'))
                count -= 1
            else:
                print(post_response('lose', player, answer, 'no'))
                break
        else:
            if check(answer):
                print(post_response('right'))
                count -= 1
            else:
                print(post_response('lose', player, answer, 'yes'))
                break
    
    if count == 0:
        print(post_response('win', player))
