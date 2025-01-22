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
        aritmetic_progression = []
        start = generate_random()
        step = random.randint(1, 10)
        random_index = random.randint(0, 9)
        for i in range(10):
            aritmetic_progression.append(start + step * i)
        result = aritmetic_progression[random_index]
        aritmetic_progression[random_index] = '..'
        print('What number is missing in the progression?')
        print('Question: ', end='')
        for i in aritmetic_progression:
            print(i, end=' ')
        print()
        user_answer = int(input('Your answer: '))    
       
        if check_answer(user_answer, result, name):
            correct_answers += 1

    congratulations(name)