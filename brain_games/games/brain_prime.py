'''Brain Prim Game: determine if a number is prime.'''

import random

from brain_games.games.launch import MINIMAL_PRIME_NUMBER, RANDOM_MAX


def game_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = random.randint(MINIMAL_PRIME_NUMBER, RANDOM_MAX)
    is_prime = all(random_number % i != 0 for i in range(2, random_number))
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return random_number, correct_answer