import random

from brain_games.games.launch import (
    CORRECT_ANSWERS_TO_WIN,
    check_answer,
    congratulations,
    generate_random,
    welcome_user,
)


def play():
    name = welcome_user()
    correct_answers = 0

    while correct_answers < CORRECT_ANSWERS_TO_WIN:
        random_number1 = generate_random()
        random_number2 = generate_random()
        symbols = ['+', '-', '*']
        random_symbol = random.choice(symbols)

        result_sum = random_number1 + random_number2
        result_diff = random_number1 - random_number2
        result_mult = random_number1 * random_number2
        
        if random_symbol == '+':
            correct_answer = result_sum
        elif random_symbol == '-':
            correct_answer = result_diff
        elif random_symbol == '*':
            correct_answer = result_mult

        print('What is the result of the expression?')
        print('Question:', random_number1, random_symbol, random_number2)

        user_answer = int(input('Your answer: '))

        if check_answer(user_answer, correct_answer, name):
            correct_answers += 1
    congratulations(name) 