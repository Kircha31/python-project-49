from brain_games.ans_que import que_ans, post_response
from brain_games.ans_que import welcome_user, number


def even_numb(numb):
    if numb % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even():
    global answer
    player = welcome_user('even_game')
    count = 3
    ans_use = 'yes'
    while count > 0:
        question = number()
        answer = que_ans(question)
        if answer not in ['yes', 'no']:
            ans_use = 'yes/no'
            break
        elif even_numb(question) == answer:
            print(post_response('right'))
            count -= 1
        else:
            ans_use = even_numb(question)
            break
    if count == 0:
        print(post_response('win', player))
    else:
        print(post_response('lose', player, answer, ans_use))
