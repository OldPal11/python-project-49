'''Brain-GCD Game: find the greatest common divisor of two numbers.'''

import math

from brain_games.games.launch import generate_random


def game_rules():
    return 'Find the greatest common divisor of given numbers.'


def generate_round():
    random_number1 = generate_random()
    random_number2 = generate_random()
    correct_answer = math.gcd(random_number1, random_number2)
    question = f'{random_number1} {random_number2}'
    return question, str(correct_answer)