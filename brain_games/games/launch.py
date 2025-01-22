import random

RANDOM_MIN = 1
RANDOM_MAX = 100
CORRECT_ANSWERS_TO_WIN = 3
MINIMAL_PRIME_NUMBER = 2


def welcome_user():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def generate_random():
    return random.randint(RANDOM_MIN, RANDOM_MAX)


def congratulations(name):
    print(f'Congratulations, {name}!')


def check_answer(user_answer, correct_answer, name):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
            )
        print(f"Let's try again, {name}!")
        exit()