import random

from brain_games.games.launch import (
    CORRECT_ANSWERS_TO_WIN,
    RANDOM_MAX,
    RANDOM_MIN,
    welcome_user,
)


def play():
    name = welcome_user()
    correct_aswers = 0
    while correct_aswers < CORRECT_ANSWERS_TO_WIN:
        random_number = random.randint(RANDOM_MIN, RANDOM_MAX)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', random_number)
        
        answer = input('Your answer: ')
        
        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            correct_aswers += 1
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
            correct_aswers += 1
        else:
            if random_number % 2 == 0:
                print(
                    f"'{answer}' is wrong answer ;(." 
                    "Correct answer was 'yes'."
                )
            else:
                print(
                    f"'{answer}' is wrong answer ;(. "
                    "Correct answer was 'no'."
                )
            print(f"Let's try again, {name}!")
            exit()

    print(f'Congratulations, {name}!')   