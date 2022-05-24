import requests
import random


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
