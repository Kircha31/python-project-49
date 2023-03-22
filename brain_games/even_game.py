import random
import prompt


def even(player):
    correct = ['yes', 'no']
    count = 3
    while count > 0:
        question = random.randint(0, 100)
        answer = prompt.string(f"Question: {question}\nYour answer: ")
        if not answer in correct:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes/no'.\n"
                  f"Let's try again, {player}!")
            break
        elif question % 2 == 0:
            if answer != correct[0]:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\n"
                      f"Let's try again, {player}!")
                break
            else:
                print('Correct!')
                count -= 1
        else:
            if answer == correct[0]:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\n"
                      f"Let's try again, {player}!")
                break
            else:
                print('Correct!')
                count -= 1
                
    if count == 0:
        print(f'Congratulations, {player}!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    return name
