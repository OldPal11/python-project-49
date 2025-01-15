import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play():
    name = welcome_user()
    correct_answers = 0
    while correct_answers < 3:
        aritmetic_progression = []
        start = random.randint(1, 100)
        step = random.randint(1, 10)
        random_index = random.randint(0, 9)
        for i in range(10):
            aritmetic_progression.append(start + step * i)
        result = aritmetic_progression[random_index]
        aritmetic_progression[random_index] = '..'
        print('What number is missing in the progression?')
        print('Question:', end='')
        for i in aritmetic_progression:
            print(i, end=' ')
        print()
        answer = int(input('Your answer: '))    
        if answer == result:
            print('Correct!')
            correct_answers += 1
        else:   
            print(
                f"'{answer}' is wrong answer ;(." 
                f"Correct answer was '{result}'."
                )       
            print(f"Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')