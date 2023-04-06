from prompt import string
from brain_games.start_game import correct_answer


def engine(game_module):
    print('Welcome to the Brain Games!')
    player = string('May I have your name? ')
    print(f'Hello, {player}!')
    print(game_module.RULES)
    count = 0
    for _ in range(3):
        question, right_answer = game_module.get_question_and_right_answer()
        user_answer = string(f'{question}\nYour answer: ')
        if correct_answer(user_answer, right_answer):
            print('Correct!')
            count += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was {right_answer}.')
            break
    if count == 3:
        print(f'Congratulations, {player}!')
    else:
        print(f"Let's try again, {player}!")
