import tkinter as tk
from tkinter import ttk
from random import sample
from tkinter import messagebox


def matrix_create():
    return {number: None for number in range(6)}


def sign_place(matrix):
    cells = list(range(6))
    signs = ['*', '&', '$']
    for sign in signs:
        element_cells = sample(cells, 2)
        for element in element_cells:
            matrix[element] = sign
            cells.remove(element)
    return matrix


class FindPairs:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('500x300')
        self.master.title('Find Pairs')
        self.master.resizable(True, True)
        self.master.bind('<KeyPress>', self.shortcut)

        self.game_matrix = None
        self.two_choices = None
        self.buttons_to_delete = None
        self.counter = None
        self.tries = None
        self.game_over = None

        self.frame = ttk.Frame(self.master)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.menu = tk.Menu(self.master)
        self.options_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Options', menu=self.options_menu)
        self.options_menu.add_command(label='Reset', command=self.reset)
        self.master.config(menu=self.menu)

        self.buttons = []
        for i in range(6):
            button = tk.Button(
                self.frame,
                text='?',
                command=lambda b=i: self.button_pressed(b),
                font='Calibri 20 bold'
            )
            button.grid(row=i//3, column=i%3, sticky="nsew")
            self.buttons.append(button)

        self.reset()
        self.master.mainloop()

    def shortcut(self, event):
        pass

    def reset(self):
        self.game_matrix = sign_place(matrix_create())
        self.two_choices = {}
        self.buttons_to_delete = []
        self.counter = 0
        self.tries = 3
        self.game_over = False
        for button in self.buttons:
            button.config(text='?', fg='black')
        self.unlock_game()

    def hide_elements(self):
        for button in self.buttons_to_delete:
            if button['fg'] != 'green':
                button.config(text='?', fg='black')
        self.buttons_to_delete.clear()

    def lock_game(self):
        for button in self.buttons:
            button['state'] = 'disabled'
        self.game_over = True

    def unlock_game(self):
        for button in self.buttons:
            button['state'] = 'normal'
        self.game_over = False

    def check_game_end(self):
        if not self.game_over:
            if all(button['fg'] == 'green' for button in self.buttons):
                messagebox.showinfo(title='Victory', message='You won, congratulations!')
                self.lock_game()
            elif self.tries == 0:
                messagebox.showinfo(title='Defeat', message='You are out of tries, try again!')
                self.lock_game()

    def button_pressed(self, index):
        button = self.buttons[index]
        if button['text'] == '?' and self.counter < 2:
            button.config(text=self.game_matrix[index])
            self.two_choices[index] = self.game_matrix[index]
            self.buttons_to_delete.append(button)
            self.counter += 1

            if self.counter == 2:
                values_list = list(self.two_choices.values())
                if values_list[0] == values_list[1]:
                    for b in self.buttons_to_delete:
                        b.config(fg='green')
                    self.two_choices.clear()
                    self.buttons_to_delete.clear()
                else:
                    self.tries -= 1
                    self.master.after(1000, self.hide_elements)
                    self.two_choices.clear()
                self.counter = 0
                self.master.after(1000, self.check_game_end)


if __name__ == '__main__':
    FindPairs()
