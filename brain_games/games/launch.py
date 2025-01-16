RANDOM_MIN = 1
RANDOM_MAX = 100
CORRECT_ANSWERS_TO_WIN = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name