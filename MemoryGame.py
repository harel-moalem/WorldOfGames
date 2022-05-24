import random
import time

def generate_sequence(difficulty):
    sequence_list = []
    min_value = 1
    max_value = 101
    for i in range(difficulty):
        sequence_list.append(random.randint(min_value, max_value))
    return sequence_list


def get_list_from_user():
    list_string = input('Enter the numbers sequence as you remember (separated with space):')
    user_sequence = []
    for number in list_string.split(' '):
        user_sequence.append(int(number))
    return user_sequence


def show_generated_sequence(generated_sequence):
    input('Hit any key to see the generated sequence. You will have a limited time to memorize it!')
    print(generated_sequence, end='')
    time.sleep(0.7)
    print('\r', end='')


def is_list_equal(generated_sequence, user_sequence):
    return generated_sequence == user_sequence


def play(difficulty):
    generated_sequence = generate_sequence(difficulty)
    show_generated_sequence(generated_sequence)
    user_sequence = get_list_from_user()
    return is_list_equal(generated_sequence, user_sequence)
