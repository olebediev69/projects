import customtkinter
from tkinter import messagebox, Menu

from customtkinter import CTkEntry

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


class TicTacToe:
    def __init__(self):
        self.turn = True
        self.winner_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

        self.root = customtkinter.CTk()

        self.root.geometry('500x200')
        self.root.resizable(False,False)
        self.root.title('Tic-Tac-Toe game')

        self.menu = Menu(self.root)
        self.root.configure(menu=self.menu)
        self.options_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Options', menu=self.options_menu)
        self.options_menu.add_command(label='Reset', command=self.reset)

        self.text = customtkinter.CTkLabel(master=self.root, font=('Arial',18), text="Tic-Tac-Toe")
        self.text.pack(pady=10,padx=10)

        self.frame = customtkinter.CTkFrame(master=self.root)

        self.btn_1 = customtkinter.CTkButton(master=self.frame,font=('Arial',18),text=' ', command=lambda: self.button_clicked(self.btn_1))
        self.btn_1.grid(column=0, row=0, padx=2, pady=2)
        self.btn_2 = customtkinter.CTkButton(master=self.frame, font=('Arial', 18),text=' ', command=lambda: self.button_clicked(self.btn_2))
        self.btn_2.grid(column=1, row=0, padx=2, pady=2)
        self.btn_3 = customtkinter.CTkButton(master=self.frame, font=('Arial', 18),text=' ', command=lambda: self.button_clicked(self.btn_3))
        self.btn_3.grid(column=2, row=0, padx=2, pady=2)
        self.btn_4 = customtkinter.CTkButton(master=self.frame, font=('Arial', 18),text=' ', command=lambda: self.button_clicked(self.btn_4))
        self.btn_4.grid(column=0, row=1, padx=2, pady=2)
        self.btn_5 = customtkinter.CTkButton(master=self.frame, font=('Arial', 18),text=' ', command=lambda: self.button_clicked(self.btn_5))
        self.btn_5.grid(column=1, row=1, padx=2, pady=2)
        self.btn_6 = customtkinter.CTkButton(master=self.frame, font=('Arial', 18),text=' ', command=lambda: self.button_clicked(self.btn_6))
        self.btn_6.grid(column=2, row=1, padx=2, pady=2)
        self.btn_7 = customtkinter.CTkButton(master=self.frame, font=('Arial', 18),text=' ', command=lambda: self.button_clicked(self.btn_7))
        self.btn_7.grid(column=0, row=2, padx=2, pady=2)
        self.btn_8 = customtkinter.CTkButton(master=self.frame, font=('Arial', 18),text=' ', command=lambda: self.button_clicked(self.btn_8))
        self.btn_8.grid(column=1, row=2, padx=2, pady=2)
        self.btn_9 = customtkinter.CTkButton(master=self.frame, font=('Arial', 18),text=' ', command=lambda: self.button_clicked(self.btn_9))
        self.btn_9.grid(column=2, row=2, padx=2, pady=2)

        self.frame.columnconfigure(index = 0, weight=1)
        self.frame.columnconfigure(index=1, weight=1)
        self.frame.columnconfigure(index=2, weight=1)
        self.frame.rowconfigure(index=0, weight=1)
        self.frame.rowconfigure(index=1, weight=1)
        self.frame.rowconfigure(index=2, weight=1)

        self.frame.pack(pady=20,padx=20)

        self.buttons = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]

        self.root.mainloop()

    def button_clicked(self, button):

        if button.cget('text') == ' ':
            if self.turn:
                button.configure(text='X',text_color='white', fg_color='darkgreen')
                self.turn = False
            else:
                button.configure(text='O', text_color='black', fg_color='darkred')
                self.turn = True
            self.check_winner(self.buttons)

    def check_winner(self,buttons):
        combinations = [(buttons[i].cget('text'), buttons[j].cget('text'), buttons[k].cget('text')) for i, j, k in self.winner_combinations]
        for combo in combinations:
            if combo[0] == combo[1] == combo[2] and combo[0] != ' ':
                messagebox.showinfo("Game Over", f"{combo[0]} wins!")
                for button in buttons:
                    button.configure(state='disabled')
                break
        else:
            if all(button.cget('text') != ' ' for button in self.buttons):
                messagebox.showinfo("Game Over", "It's a draw!")
                for button in buttons:
                    button.configure(state='disabled')

    def reset(self):
        for button in self.buttons:
            button.configure(state='normal', text=' ', fg_color='#20548c')


if __name__ == '__main__':
    TicTacToe()