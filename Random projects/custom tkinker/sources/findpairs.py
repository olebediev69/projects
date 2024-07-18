import tkinter as tk
import customtkinter
from random import sample
from tkinter import messagebox

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')


# matrix block
def create_matrix():
    return {a: None for a in range(1, 7)}


def place_signs(matrix):
    cells = list(matrix.keys())
    for sign in ["*", "/", "#"]:
        placement_cells = sample(cells, 2)
        for i in placement_cells:
            matrix[i] = sign
            cells.remove(i)
    return matrix


class FindPairs:

    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('500x350')
        self.master.title("Find Pairs game")

        # menu
        self.menu = tk.Menu(master=self.master)
        self.master.configure(menu=self.menu)
        self.options_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Options', menu=self.options_menu)
        self.options_menu.add_command(label='Reset', command=self.reset_game)

        # additional variables
        self.counter = 0
        self.similarity = set()
        self.buttons_pressed = set()
        self.tries = 4

        # matrix debug
        self.main_matrix = place_signs(create_matrix())

        # frame
        self.frame = customtkinter.CTkFrame(
            master=self.master
        )
        self.frame.columnconfigure([0, 1, 2], weight=1)
        self.frame.rowconfigure([0, 1], weight=1)

        # buttons
        self.btn1 = customtkinter.CTkButton(
            master=self.frame,
            text='?',
            font=('Calibri', 20, 'bold'),
            fg_color='black',
            hover_color='gray',
            command=lambda: self.button_pressed(self.btn1, 1)
        )
        self.btn1.grid(row=0, column=0, sticky='news', padx=2, pady=2)

        self.btn2 = customtkinter.CTkButton(
            master=self.frame,
            text='?',
            font=('Calibri', 20, 'bold'),
            fg_color='black',
            hover_color='gray',
            command=lambda: self.button_pressed(self.btn2, 2)
        )
        self.btn2.grid(row=0, column=1, sticky='news', padx=2, pady=2)

        self.btn3 = customtkinter.CTkButton(
            master=self.frame,
            text='?',
            font=('Calibri', 20, 'bold'),
            fg_color='black',
            hover_color='gray',
            command=lambda: self.button_pressed(self.btn3, 3)
        )
        self.btn3.grid(row=0, column=2, sticky='news', padx=2, pady=2)

        self.btn4 = customtkinter.CTkButton(
            master=self.frame,
            text='?',
            font=('Calibri', 20, 'bold'),
            fg_color='black',
            hover_color='gray',
            command=lambda: self.button_pressed(self.btn4, 4)
        )
        self.btn4.grid(row=1, column=0, sticky='news', padx=2, pady=2)

        self.btn5 = customtkinter.CTkButton(
            master=self.frame,
            text='?',
            font=('Calibri', 20, 'bold'),
            fg_color='black',
            hover_color='gray',
            command=lambda: self.button_pressed(self.btn5, 5)
        )
        self.btn5.grid(row=1, column=1, sticky='news', padx=2, pady=2)

        self.btn6 = customtkinter.CTkButton(
            master=self.frame,
            text='?',
            font=('Calibri', 20, 'bold'),
            fg_color='black',
            hover_color='gray',
            command=lambda: self.button_pressed(self.btn6, 6)
        )
        self.btn6.grid(row=1, column=2, sticky='news', padx=2, pady=2)

        self.buttons_list = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6]
        self.frame.pack(padx=10, pady=10, fill='both', expand=True)

        self.master.mainloop()

    def reset_game(self):
        self.main_matrix = place_signs(create_matrix())
        self.unlock_buttons()
        self.tries = 4

    def show_buttons(self):
        for index, button in enumerate(self.buttons_list, start=1):
            button.configure(text=self.main_matrix[index], fg_color='darkred')

    def block_buttons(self):
        for button in self.buttons_list:
            button.configure(state='disabled')

    def unlock_buttons(self):
        for button in self.buttons_list:
            button.configure(state='normal', text='?', fg_color='black')

    def victory_check(self):
        if all(button.cget('fg_color') == 'darkgreen' for button in self.buttons_list):
            messagebox.showinfo('Victory', 'You have guessed all signs!')
            self.block_buttons()
        elif self.tries == 0:
            messagebox.showinfo('Defeat', "You haven't guessed all signs!")
            self.block_buttons()
            self.master.after(100, self.show_buttons)

    def paint_button(self, color):
        for button in self.buttons_pressed:
            button.configure(fg_color=color)

    def hide_buttons(self):
        for button in self.buttons_pressed:
            button.configure(text='?', fg_color='black')
        self.counter = 0
        self.buttons_pressed.clear()
        self.similarity.clear()

    def reveal_button(self, button, matrix, index_for_matrix):
        if button.cget('text') == '?':
            button.configure(text=matrix[index_for_matrix])
            self.counter += 1
            self.similarity.add(matrix[index_for_matrix])
            self.buttons_pressed.add(button)

    def button_pressed(self, button, index):
        self.reveal_button(button, self.main_matrix, index)
        if self.counter == 2:
            if len(self.similarity) == 1:
                self.paint_button('darkgreen')
                self.counter = 0
                self.similarity.clear()
                self.buttons_pressed.clear()
            else:
                self.paint_button('darkred')
                self.master.after(1000, self.hide_buttons)
                self.tries -= 1
        self.master.after(200, self.victory_check)


if __name__ == '__main__':
    FindPairs()
