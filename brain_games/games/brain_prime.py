import random

from brain_games.games.launch import (
    CORRECT_ANSWERS_TO_WIN,
    MINIMAL_PRIME_NUMBER,
    RANDOM_MAX,
    welcome_user,
)


def play():
    name = welcome_user()
    correct_aswers = 0
    while correct_aswers < CORRECT_ANSWERS_TO_WIN:
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
        answer = input('Your answer: ')
        if answer == result:
            print('Correct!')
            correct_aswers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(." 
                f"Correct answer was '{result}'."
                )
            print(f"Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')