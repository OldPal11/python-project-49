'''Even Game: Even or not?'''


from brain_games.games.launch import generate_random


def game_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = generate_random()
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, correct_answer 