import tkinter as tk
from tkinter import ttk
from random import sample

class FindPairs:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('500x300')
        self.master.title('Find Pairs')
        self.master.resizable(True, True)
        self.master.bind('KeyPress', self.shortcut)

        self.frame = ttk.Frame(self.master)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)

        self.game_matrix = self.sign_place(self.matrix_create())
        self.two_choices = {}
        self.buttons_to_delete = []
        self.counter = 0

        # Adjust the lambda to correctly capture the current button in each iteration
        self.buttons = []
        for i in range(6):
            button = ttk.Button(
                master=self.frame,
                text='?',
                command=lambda b=button: self.button_pressed(b, self.game_matrix, b.grid_info()['row'] * 3 + b.grid_info()['column'] + 1),
                style='TButton'
            )
            button.grid(row=i//3, column=i%3, sticky="nsew")
            self.buttons.append(button)

        self.frame.pack(fill=tk.BOTH, expand=True)
        self.master.mainloop()

    def shortcut(self, event):
        pass

    def matrix_create(self):
        matrix = {number: None for number in range(1, 7)}
        return matrix

    def two_choice_clear(self, matrix):
        if len(matrix) > 1:
            matrix.clear()
        return matrix

    def hide_elements(self, buttons_list):
        for button in buttons_list:
            button.config(text='?')

    def button_pressed(self, button, matrix, index):
        if button.cget('text') == '?':
            if self.counter < 2:
                self.buttons_to_delete.append(button)
                button.config(text=matrix[index])
                self.two_choice_clear(self.two_choices)
                self.two_choices[index] = matrix[index]

                self.counter += 1

                if len(self.two_choices) == 2:
                    values_list = list(self.two_choices.values())
                    if values_list[0] == values_list[1]:
                        self.counter = 0
                        for element in self.buttons_to_delete:
                            element.config(foreground='green')
                        self.buttons_to_delete.clear()
                    else:
                        self.master.update()
                        self.master.after(1500, lambda: self.hide_elements(self.buttons_to_delete))
                        self.counter = 0
                        self.buttons_to_delete.clear()

        return self.counter, self.two_choices

    def sign_place(self, matrix):
        cells = [i for i in range(1, 7)]
        for sign in ['*', '&', '$']:
            element_cells = sample(cells, 2)
            for element in element_cells:
                matrix[element] = sign
                cells.remove(element)

        return matrix

if __name__ == '__main__':
    FindPairs()
