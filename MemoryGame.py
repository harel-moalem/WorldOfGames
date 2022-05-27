import random
import time
from tkinter import *
from tkinter import ttk

class FrameData:

    current_row = 0

    def __init__(self, frame, difficulty):
        self.frame = frame
        self.generated_numbers = generate_sequence(difficulty)
        self.message = StringVar()
        self.numbers_label_text = StringVar()
        self.result_label_text = StringVar()

        self.message_label = self.draw_label()
        self.set_label_text('Press `go` to see the generated sequence. You will have a limited time to memorize it!')
        self.go_btn = self.init_game_button()
        self.numbers_label = self.init_numbers_label()
        self.result_label = ttk.Label(self.frame, style='main.TLabel', textvariable=self.result_label_text)


    def add_row(self):
        row = self.current_row
        self.current_row += 1
        return row

    def remove_row(self):
        row = self.current_row
        self.current_row -= 1
        return row

    def set_label_text(self, msg):
        self.message.set(msg)

    def draw_label(self):
        message_label = ttk.Label(self.frame, textvariable=self.message, style='main.TLabel')
        message_label.grid(row=self.add_row(), pady='0 15', columnspan=len(self.generated_numbers))
        return message_label

    def init_game_button(self):
        go_btn = ttk.Button(self.frame, style='main.TButton', padding='10 5', text='Go!',
                            command=self.show_numbers)
        go_btn.grid(row=self.add_row(), columnspan=len(self.generated_numbers))
        return go_btn

    def init_numbers_label(self):
        numbers_label = ttk.Label(self.frame, style='sequence.TLabel', textvariable=self.numbers_label_text)
        return numbers_label

    def show_numbers(self):
        self.numbers_label.grid(row=self.add_row(), pady=15, columnspan=len(self.generated_numbers))
        self.numbers_label_text.set('  '.join([str(num) for num in self.generated_numbers]))
        self.numbers_label.after(1000, self.hide_numbers)

    def hide_numbers(self):
        self.numbers_label.destroy()
        self.remove_row()
        self.set_label_text('Enter the numbers as you remember below:')
        self.draw_inputs()

    def draw_inputs(self):
        inputs_row = self.add_row()
        for i in range(len(self.generated_numbers)):
            ttk.Entry(self.frame, style='input.TEntry', font='helvetica 18', width=5).grid(row=inputs_row, column=i)

        self.go_btn.configure(text='Guess!', command=self.check_numbers)
        self.go_btn.grid(row=self.add_row(), pady='15 0', columnspan=len(self.generated_numbers))

    def check_numbers(self):
        children_widgets = self.frame.winfo_children()
        number_from_user = []
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'TEntry':
                try:
                    number_from_user.append(int(child_widget.get()))
                except ValueError:
                    self.result_label_text.set('Invalid input, please check you entered numbers and try again')

        if self.generated_numbers == number_from_user:
            self.result_label_text.set('Well done!')
        else:
            self.result_label_text.set('Wrong, try again')

        self.result_label.grid(row=self.add_row(), columnspan=len(self.generated_numbers))


def play_gui(frame, difficulty):
    FrameData(frame, difficulty)



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
