import tkinter as tk
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.winner_pos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        self.winner = False
        self.turn = 0

        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('Tic-Tac-Toe')
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text='Tic-Tac-Toe', fg='White', bg='Black')
        self.label.pack(padx=10, pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)

        self.btn1 = tk.Button(self.frame, width=3, height=2)
        self.btn1.grid(row=0, column=0)

        self.btn2 = tk.Button(self.frame, width=3, height=2)
        self.btn2.grid(row=0, column=1)

        self.btn3 = tk.Button(self.frame, width=3, height=2)
        self.btn3.grid(row=0, column=2)

        self.btn4 = tk.Button(self.frame, width=3, height=2)
        self.btn4.grid(row=1, column=0)

        self.btn5 = tk.Button(self.frame, width=3, height=2)
        self.btn5.grid(row=1, column=1)

        self.btn6 = tk.Button(self.frame, width=3, height=2)
        self.btn6.grid(row=1, column=2)

        self.btn7 = tk.Button(self.frame, width=3, height=2)
        self.btn7.grid(row=2, column=0)

        self.btn8 = tk.Button(self.frame, width=3, height=2)
        self.btn8.grid(row=2, column=1)

        self.btn9 = tk.Button(self.frame, width=3, height=2)
        self.btn9.grid(row=2, column=2)

        self.frame.pack(pady=20)

        self.quit_button = tk.Button(self.root, text='Restart', command=self.restart)
        self.quit_button.pack(padx=10, pady=30)

        self.root.mainloop()

    def winner_logic(self):
        pass

    def move(self):
        pass



    def char_replacement(self):
        pass

    def restart(self):
        print('Restarting...')


GUI()
