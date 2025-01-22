import math

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
        result_gcd = math.gcd(random_number1, random_number2)
        print('Find the greatest common divisor of given numbers.')
        print('Question:', random_number1, random_number2)
        
        user_answer = int(input('Your answer: '))
        
        if check_answer(user_answer, result_gcd, name):
            correct_answers += 1
    congratulations(name)  