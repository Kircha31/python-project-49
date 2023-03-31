from random import randint
from prompt import string


# generate random number
def number():
    question = randint(0, 100)
    return question


# Greet users
def welcome_user():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
