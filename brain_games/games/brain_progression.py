'''Progression Game: find the missing number in the progression.'''

import random

from brain_games.games.launch import generate_random


def game_rules():
    return 'What number is missing in the progression?'


def generate_round():
    progression = []
    progression_step = random.randint(1, 10)
    progression_length = 10
    progression_start = generate_random()
    progression.append(progression_start)

    for i in range(1, progression_length):
        progression.append(progression[i - 1] + progression_step)

    hidden_element_index = random.randint(0, progression_length - 1)
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    question = ' '.join(map(str, progression))

    return question, str(correct_answer)