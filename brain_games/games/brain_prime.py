import random

from brain_games.games.launch import (
    CORRECT_ANSWERS_TO_WIN,
    MINIMAL_PRIME_NUMBER,
    RANDOM_MAX,
    check_answer,
    congratulations,
    welcome_user,
)


def play():
    name = welcome_user()
    correct_answers = 0
    while correct_answers < CORRECT_ANSWERS_TO_WIN:
        random_number = random.randint(MINIMAL_PRIME_NUMBER, RANDOM_MAX)
        is_prime = True
        for i in range(MINIMAL_PRIME_NUMBER, random_number):
            if random_number % i == 0:
                is_prime = False
                break
        if is_prime:
            result = 'yes'
        else:
            result = 'no'
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print('Question:', random_number)
        user_answer = input('Your answer: ')

        if check_answer(user_answer, result, name):
            correct_answers += 1

    congratulations(name)