import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play():
    name = welcome_user()
    correct_aswers = 0
    while correct_aswers < 3:
        random_number = random.randint(1, 100)
        is_prime = True
        for i in range(2, random_number):
            if random_number % i == 0:
                is_prime = False
                break
        if is_prime:
            result = 'yes'
        else:
            result = 'no'
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print('Question: ', random_number)
        answer = input('Your answer: ')
        if answer == result:
            print('Correct!')
            correct_aswers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(." 
                f"Correct answer was '{result}'."
                )
            print(f"Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')