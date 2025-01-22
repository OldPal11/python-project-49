
from brain_games.games.launch import (
    CORRECT_ANSWERS_TO_WIN,
    check_answer,
    congratulations,
    generate_random,
    welcome_user,
)


def play():
    name = welcome_user()
    correct_aswers = 0
    while correct_aswers < CORRECT_ANSWERS_TO_WIN:
        random_number = generate_random()
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', random_number)
        
        user_answer = input('Your answer: ')
        
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        if check_answer(user_answer, correct_answer, name):
            correct_aswers += 1

    congratulations(name)  