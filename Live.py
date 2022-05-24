from GuessGame import play as guess_game
from MemoryGame import  play as memory_game
from CurrencyRouletteGame import play as currency_roulette_game

def welcome(name):
    return f"Hello {name} and welcome to the World of Games(WoG).\nHere you can find many cool games to play."


def is_valid_choice(input_string, min_val, max_val):
    if input_string.isdigit():
        int_value = int(input_string)
        return min_val <= int_value <= max_val
    return False


def load_game():
    print("Please choose a game to play:")
    print("\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("\t2. Guess Game - guess a number and see if you chose like the computer")
    print("\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    user_game_choice = input('')

    while not is_valid_choice(user_game_choice, 1, 3):
        user_game_choice = input(f'Invalid choice. Please value between 1 and 3:')

    user_difficulty_choice = input('Please choose game difficulty from 1 to 5:')

    while not is_valid_choice(user_difficulty_choice, 1, 5):
        user_difficulty_choice = input('Invalid value. Please choose game difficulty from 1 to 5:')
    play_game(int(user_game_choice), int(user_difficulty_choice))


def play_game(game, difficulty):
    try:
        if game == 1:
            print(memory_game(difficulty))
        elif game == 2:
            print(guess_game(difficulty))
        else:
            print(currency_roulette_game(difficulty))
    except Exception as e:
        print(f'An error occurred: {e}')
