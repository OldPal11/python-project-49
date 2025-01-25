'''Calculation Game: calculate the result of the expression.'''

import random

from brain_games.games.launch import generate_random


def game_rules():
    return 'What is the result of the expression?'


def generate_round():
    random_number1 = generate_random()
    random_number2 = generate_random()
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f'{random_number1} {operator} {random_number2}'
    if operator == '+':
        correct_answer = random_number1 + random_number2
    elif operator == '-':
        correct_answer = random_number1 - random_number2
    else:
        correct_answer = random_number1 * random_number2
    return question, str(correct_answer)