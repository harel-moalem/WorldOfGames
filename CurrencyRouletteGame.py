import requests
import random
import tkinter as tk
from tkinter import ttk


class GameGui:
    main_label_text = None
    main_label = None
    main_entry = None
    main_button = None
    msg_label = None
    msg_label_text = None
    convertedUSD = None
    margin_error_threshold = 5

    def __init__(self, frame, difficulty, callback):
        self.current_row = 0
        self.callback = callback
        self.difficulty = difficulty
        self.frame = frame
        self.frame.columnconfigure(0, weight=1)
        self.randomPriceILS = generate_amount()
        self.set_main_label(f'Try to guess how much is {self.randomPriceILS} ILS in USD.'
                            f' Your margin of error is [+-{self.margin_error_threshold - self.difficulty}]')
        self.set_text_input()
        self.set_button()

        self.set_messages_label()
        self.frame.after(500, self.set_converted_price)

    def set_converted_price(self):
        self.convertedUSD = get_currency_converted(self.randomPriceILS)

    def check(self):
        user_input = self.get_entry_input()
        if user_input > -1:
            if is_guess_right(self.convertedUSD, user_input, self.difficulty):
                self.set_messages_label_text('Great job!')
                if self.callback:
                    self.callback()
            else:
                self.set_messages_label_text(f'Guess is not exact enough, the USD value is ${self.convertedUSD}')
            self.disable_game()

    def disable_game(self):
        self.main_entry.config(state=tk.DISABLED)
        self.main_button.config(state=tk.DISABLED)

    def set_messages_label_text(self, text):
        self.msg_label.config(text=text)

    def set_messages_label(self):
        self.msg_label = ttk.Label(self.frame, text='', style='main.TLabel')
        self.msg_label.grid(row=3, pady='5 15', column=0)

    def set_button(self):
        self.main_button = ttk.Button(self.frame, style='main.TButton', text='Go', command=self.check)
        self.main_button.grid(row=2, pady='0 10', column=0)

    def get_entry_input(self):
        try:
            return float(self.main_entry.get())
        except ValueError:
            self.set_messages_label_text(f'value {self.main_entry.get()} is not a valid number!')
            return -1

    def set_text_input(self):
        self.main_entry = ttk.Entry(self.frame, width=15)
        self.main_entry.grid(row=1, pady=10, column=0)

    def set_main_label(self, text):
        self.main_label = ttk.Label(self.frame, text=text, style='main.TLabel')
        self.main_label.grid(row=0, column=0)

    def set_main_label_text(self, text):
        self.main_label_text.set(text)


def play_game_gui(frame, difficulty, callback):
    GameGui(frame, difficulty, callback)


def generate_amount(min_value=1, max_value=100):
    return random.randint(min_value, max_value)


def get_guess_from_user(amount):
    user_guess = input(f'Enter how much you think are {amount} ILS in USD:')
    return float(user_guess)


def is_guess_right(amount, user_guess, difficulty):
    interval = get_money_interval(amount, difficulty)
    return interval[0] <= user_guess <= interval[1]


def get_money_interval(amount, difficulty):
    error_margin = 5 - difficulty
    return amount - error_margin, amount + error_margin


def get_currency_converted(amount, currency_from='ILS', currency_to='USD'):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
    payload = {}
    headers = {
        "apikey": "wKL1A31pOzePEiDLeCtTIDiYbnhpoJpS"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    return result['result']


def play(difficulty):
    amount = generate_amount()
    amount_converted = get_currency_converted(amount)
    user_guess = get_guess_from_user(amount)
    return is_guess_right(amount_converted, user_guess, difficulty)
