import random
from tkinter import *


def play_gui(difficulty, frame):
    secret_number = generate_number(difficulty)
    draw_gui(frame, difficulty)


def play(difficulty):
    secret_number = generate_number(difficulty)
    return compare_results(get_guess_from_user(difficulty), generate_number(difficulty))


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    return int(input(f'Please enter a number between 1 and {difficulty}:'))


def compare_results(user_input, secret_number):
    return user_input == secret_number


def draw_gui(frame, difficulty):
    label = Label(frame, text=f"A number between 1-{difficulty} has been generated. Try to guess it!")
    label.grid(row=0, columnspan=difficulty)
    # buttons
    for i in range(difficulty):
        button = Button(frame, text=(i + 1), padx=10, pady=10)
        button.grid(row=2, column=i)


def button_clicked(value):
    print(value)

