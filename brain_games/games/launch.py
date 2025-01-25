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


def run_game(generate_round, game_rules):
    name = welcome_user()
    print(game_rules) 
    correct_answers = 0

    while correct_answers < CORRECT_ANSWERS_TO_WIN:
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if check_answer(user_answer, correct_answer, name):
            correct_answers += 1
    congratulations(name)