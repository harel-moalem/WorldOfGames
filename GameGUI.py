from tkinter import *
from tkinter import ttk
from GuessGame import play_gui as guess_game_play
from MemoryGame import play_gui as memory_game_play
from CurrencyRouletteGame import play_game_gui as currency_play_gui
from Score import add_score

class GUI:

    def set_main_header(self, text):
        self.header_label_text.set(text)

    def init_header(self):
        self.header_label_text = StringVar()
        self.set_main_header("Hello, and welcome to the World Of Games!")
        self.header_label = ttk.Label(self.mainframe, textvariable=self.header_label_text, style='Header.Label')
        self.header_label.grid(row=0, sticky=(N, E, W, S), pady='0 20')

    def init_select_box(self, options):
        select_frame = ttk.Frame(self.mainframe, padding="10", style='main.TFrame')
        select_frame.grid(row=options['row'])
        select_box_val = StringVar()
        select_box_options = options['options']
        select_box_val.set(select_box_options[0])
        ttk.Label(select_frame, text=options['text'], style='main.TLabel').grid(row=0, column=0, padx=15)
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

        self.game_frame = ttk.Frame(self.mainframe, style='main.TFrame')
        self.game_frame.grid(row=6, columnspan=2)
        callback = lambda: add_score(difficulty)
        if game == 'Guess Game':
            guess_game_play(difficulty, self.game_frame, callback)
        elif game == 'Memory Game':
            memory_game_play(self.game_frame, difficulty, callback)
        else:
            currency_play_gui(self.game_frame, difficulty, callback)

    def draw_separator(self):
        separator = ttk.Separator(self.mainframe, orient='horizontal')
        separator.grid(row=5, columnspan=2, column=0, sticky='ew', pady=15)

    def __init__(self):
        self.header_label = None
        self.header_label_text = None
        self.game_frame = None
        self.root = Tk(className='World of games')
        self.BG = '#3572A5'
        self.root.title('world of games')
        self.root.configure(background=self.BG, pady=20, padx=20)
        self.s = ttk.Style()
        self.s.configure('Header.Label', font='helvetica 18', foreground='#ffffff',
                         relief='raised', background=self.BG)
        self.frame_style = ttk.Style()
        self.frame_style.configure('main.TFrame', background=self.BG)
        self.default_label_style = ttk.Style()
        self.default_label_style.configure('main.TLabel', background=self.BG, foreground='#ffffff')
        self.big_label_style = ttk.Style()
        self.big_label_style.configure('sequence.TLabel', font='helvetica 24', foreground='#333333', padding='20')
        self.input_style = ttk.Style()
        self.input_style.configure('input.TEntry', font='helvetica 18', foreground='#333333')

        self.options_style = ttk.Style()
        self.options_style.configure('main.OptionMenu', background=self.BG)

        self.mainframe = ttk.Frame(self.root, style='main.TFrame')
        self.mainframe.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        game_options = ["Memory Game", "Guess Game", "CurrencyRoulette"]
        difficulty_options = ["1", "2", "3", "4", "5"]

        self.init_header()
        self.game_select = self.init_select_box({"row": 1, "options": game_options, "text": "Select game:"})
        self.difficulty_select = self.init_select_box({"row": 2, "options": difficulty_options, "text": "Select difficulty:"})
        self.draw_play_button()
        self.draw_separator()
        self.root.mainloop()

GUI()