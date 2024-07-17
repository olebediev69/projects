import customtkinter
from sources.tictactoe import TicTacToe
from sources.authentication import Login
from sources.findpairs import FindPairs


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


class Launcher:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title('Projects Launcher')
        self.root.geometry('500x200')

        self.label = customtkinter.CTkLabel(self.root, text='Choose a project you want to start:', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.start_option = customtkinter.StringVar(value='')
        self.option_select = customtkinter.CTkOptionMenu(self.root, values=['', 'Tic-Tac-Toe','Find Pairs'],
                                                         variable=self.start_option)
        self.option_select.pack(padx=10, pady=10)

        self.button = customtkinter.CTkButton(self.root, text='Enter choice', command=self.select_choice)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def select_choice(self):
        if self.option_select.get() == 'Tic-Tac-Toe':
            TicTacToe()
        elif self.option_select.get() == 'Find Pairs':
            FindPairs()


if Login():
    Launcher()
