import customtkinter
import tkinter as tk
from random import choice


class Hangman:

    def __init__(self):
        self.master = tk.Tk()
        self.master.title('Hangman')
        self.master.geometry('500x600')
        self.master.resizable(False, False)

        self.deadman = ['  0 ', '--|--', '  |  ', ' / \ ']
        self.words = ['apple', 'banana', 'something']
        self.selected_word = choice(self.words)

        self.label = customtkinter.CTkLabel(
            master=self.master,
            text='Hangman game',
            font=('Calibri', 35, 'bold')
        )
        self.label.pack(padx=10, pady=(30, 20))

        self.text_field = customtkinter.CTkEntry(
            master=self.master,
            placeholder_text='Enter a word'
        )
        self.text_field.pack(padx=10, pady=(0, 10))

        self.show_result_var = tk.StringVar()
        self.show_result = customtkinter.CTkLabel(
            master=self.master,
            textvariable=self.show_result_var,
            font=('Calibri', 15, 'bold')
        )
        self.show_result.pack(padx=10, pady=(0, 10))

        self.accept_button = customtkinter.CTkButton(
            master=self.master,
            text='Try',
            command=self.accept_button
        )
        self.accept_button.pack(padx=10, pady=(0, 10))

        self.master.mainloop()

    def accept_button(self):
        self.show_result_var.set(self.text_field.get())

Hangman()
