import math
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
        random_number1 = random.randint(1, 100)
        random_number2 = random.randint(1, 100)
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