from tkinter import *
from tkinter import ttk


from GuessGame import play_gui as guess_game_play

class GUI:

    def set_main_header(self, text):
        self.header_label_text.set(text)

    def init_header(self):
        self.header_label_text = StringVar()
        self.set_main_header("Hello, and welcome to the World Of Games!")
        self.header_label = ttk.Label(self.mainframe, textvariable=self.header_label_text, style='Header.Label')
        self.header_label.grid(row=0, sticky=(N, E, W, S))

    def init_select_box(self, options):
        select_frame = ttk.Frame(self.mainframe, padding="10")
        select_frame.grid(row=options['row'])
        select_box_val = StringVar()
        select_box_options = options['options']
        select_box_val.set(select_box_options[0])
        Label(select_frame, text=options['text']).grid(row=0, column=0)
        options_menu = OptionMenu(select_frame, select_box_val, *options["options"])
        options_menu.grid(row=0, column=1)
        return select_box_val

    def draw_play_button(self):
        Button(self.mainframe, text="Play!", padx=15, command=self.play_clicked).grid(row=4, padx=10)

    def play_clicked(self):
        difficulty = int(self.difficulty_select.get())
        game = self.game_select.get()
        if self.game_frame is not None:
            self.game_frame.destroy()

        if game == 'Guess Game':
            self.game_frame = ttk.Frame(self.mainframe, padding=20)
            self.game_frame.grid(row=6, columnspan=2)
            guess_game_play(difficulty, self.game_frame)

    def draw_separator(self):
        separator = ttk.Separator(self.mainframe, orient='horizontal')
        separator.grid(row=5, columnspan=2)



    def __init__(self):
        self.header_label = None
        self.header_label_text = None
        self.game_frame = None
        self.root = Tk()
        self.root.title('world of games')
        self.s = ttk.Style()
        self.s.configure('Header.Label', font='helvetica 18', foreground='gray', padx=10, pady=10)
        s = ttk.Style()
        s.configure("C.Tk", background="")
        self.mainframe = Frame(self.root, bg="#d09cdf", padx=15, pady=15)
        self.mainframe.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        game_options = ["Memory Game", "Guess Game", "CurrencyRoulette"]
        difficulty_options = ["1", "2", "3", "4", "5"]

        self.init_header()
        self.game_select = self.init_select_box({"row": 1, "options": game_options, "text": "Select game:"})
        self.difficulty_select = self.init_select_box({"row": 2, "options": difficulty_options, "text": "Select difficulty:"})
        self.draw_play_button()
        self.draw_separator()
        self.root.mainloop()

GUI()