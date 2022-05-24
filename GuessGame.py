import random
from tkinter import *
from tkinter import ttk

def play_gui(difficulty, frame):
    secret_number = generate_number(difficulty)
    draw_gui(frame, difficulty, secret_number)


def play(difficulty):
    secret_number = generate_number(difficulty)
    return compare_results(get_guess_from_user(difficulty), generate_number(difficulty))


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    return int(input(f'Please enter a number between 1 and {difficulty}:'))


def compare_results(user_input, secret_number):
    return user_input == secret_number


def draw_gui(frame, difficulty, secret_number):
    label = ttk.Label(frame, text=f"A number between 1-{difficulty} has been generated. Try to guess it!",
                      style='main.TLabel')
    label.grid(row=0, columnspan=difficulty, pady='0 20')
    # message label
    message = StringVar()
    ttk.Label(frame, textvariable=message, style='main.TLabel').grid(row=2, columnspan=difficulty, pady='10 0')
    # buttons
    for i in range(difficulty):
        button = Button(frame, text=(i + 1), padx=10, pady=10,
                        command=lambda arg=i: button_clicked(arg + 1, secret_number, message))
        button.grid(row=1, column=i)


def button_clicked(value, secret_number, message):
    if compare_results(value, secret_number):
        message.set('Well done!')
    else:
        message.set('Nope. Better luck next time!')



