'''Brain Prim Game: determine if a number is prime.'''

import random

from brain_games.games.launch import MINIMAL_PRIME_NUMBER, RANDOM_MAX


def game_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_round():
    random_number = random.randint(MINIMAL_PRIME_NUMBER, RANDOM_MAX)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return random_number, correct_answer