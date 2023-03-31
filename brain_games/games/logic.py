from prompt import string


def correct_answer(numb, correct):
    user_answer = string(f"Question: {numb}\nYour answer: ")
    if correct == user_answer:
        print('Correct!')
        return True
    else:
        print(f'\'{user_answer}\' is wrong answer ;(. '
              f'Correct answer was {correct}.')
        return False
