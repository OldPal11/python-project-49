from brain_games.games.brain_prime import game_rules, generate_round
from brain_games.games.launch import run_game


def main():
    run_game(generate_round, game_rules())


if __name__ == "__main__":
    main()