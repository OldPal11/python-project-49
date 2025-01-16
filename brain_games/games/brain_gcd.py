import math
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
        result_gcd = math.gcd(random_number1, random_number2)
        print('Find the greatest common divisor of given numbers.')
        print('Question:', random_number1, random_number2)
        
        answer = int(input('Your answer: '))
        
        if answer == result_gcd:
            print('Correct!')
            correct_answers += 1
        else:   
            print(
                f"'{answer}' is wrong answer ;(." 
                f"Correct answer was '{result_gcd}'."
                )       
            print(f"Let's try again, {name}!")
            exit()

    print(f'Congratulations, {name}!')   