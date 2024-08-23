import tkinter as tk
import customtkinter


class MCalculator:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('300x200')
        self.master.title('Minecraft stacks calculator')
        self.master.resizable(False, False)

        self.master.bind('<KeyPress>', self.enter)

        self.label = customtkinter.CTkLabel(
            master=self.master,
            text='Quantity:',
            font=('Calibri', 20, 'bold')
        )
        self.label.pack(
            padx=10,
            pady=(30, 10),
        )

        self.entry_var = tk.StringVar()
        self.entry = customtkinter.CTkEntry(
            master=self.master,
            textvariable=self.entry_var,
            font=('Calibri', 15)
        )
        self.entry.pack(
            padx=10,
            pady=10,
        )

        self.button = customtkinter.CTkButton(
            master=self.master,
            text='Calculate',
            font=('Calibri', 15),
            command=self.calculate
        )
        self.button.pack(
            padx=10,
            pady=(10, 0)
        )

        self.result_var = tk.StringVar()
        self.result = customtkinter.CTkLabel(
            master=self.master,
            text='',
            font=('Calibri', 10),
            textvariable=self.result_var,
        )
        self.result.pack(
            padx=10,
            pady=(0, 10),
        )

        self.master.mainloop()

    def calculate(self):
        entered_value = self.entry_var.get()
        if entered_value.isdigit():
            stacks = int(entered_value) // 64
            remaining_value = int(entered_value) - stacks * 64
            self.result_var.set(f'{stacks} stacks and {remaining_value}')
        else:
            self.result_var.set('Please enter a valid number')

    def enter(self, event):
        if event.keysym == 'Return':
            self.button.invoke()


if __name__ == '__main__':
    MCalculator()
