import random

from brain_games.games.launch import (
    CORRECT_ANSWERS_TO_WIN,
    RANDOM_MAX,
    RANDOM_MIN,
    welcome_user,
)


def play():
    name = welcome_user()
    correct_answers = 0
    while correct_answers < CORRECT_ANSWERS_TO_WIN:
        random_number1 = random.randint(RANDOM_MIN, RANDOM_MAX)
        random_number2 = random.randint(RANDOM_MIN, RANDOM_MAX)
        symbols = ['+', '-', '*']
        random_symbol = random.choice(symbols)
        result_sum = random_number1 + random_number2
        result_diff = random_number1 - random_number2
        result_mult = random_number1 * random_number2
        print('What is the result of the expression?')
        print('Question:', random_number1, random_symbol, random_number2)
        
        answer = int(input('Your answer: '))
        
        if random_symbol == '+' and answer == result_sum:
            print('Correct!')
            correct_answers += 1
        elif random_symbol == '-' and answer == result_diff:
            print('Correct!')
            correct_answers += 1
        elif random_symbol == '*' and answer == result_mult:
            print('Correct!')
            correct_answers += 1
        else:
            if random_symbol == '+':
                print(
                    f"'{answer}' is wrong answer ;(." 
                    f"Correct answer was' {result_sum}'."
                )
            elif random_symbol == '-':
                print(
                    f"'{answer}' is wrong answer ;(." 
                    f"Correct answer was' {result_diff}'."
                )
            elif random_symbol == '*':
                print(
                    f"'{answer}' is wrong answer ;(." 
                    f" Correct answer was '{result_mult}'."
                )       
            print(f"Let's try again, {name}!")
            exit()

    print(f'Congratulations, {name}!')   