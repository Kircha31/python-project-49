from brain_games.ans_que import *


def even():
    global answer
    player = welcome_user('even_game')
    count = 3
    ans_use = ''
    while count > 0:
        question = number()
        answer = que_ans(question)
        if answer not in ['yes', 'no']:
            ans_use = 'yes/no'
            break
        elif question % 2 == 0:
            if check(answer):
                print(post_response('right'))
                count -= 1
            else:
                ans_use = 'no'
                break
        else:
            if not check(answer):
                print(post_response('right'))
                count -= 1
            else:
                ans_use = 'yes'
                break
    
    if count == 0:
        print(post_response('win', player))
    else:
        print(post_response('lose', player, answer, ans_use))
        
