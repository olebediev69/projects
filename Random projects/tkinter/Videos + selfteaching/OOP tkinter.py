import tkinter as tk
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('First interface')
        self.root.geometry('500x500')
        self.root.resizable(False, False)

        # event reading (current event = pressing key)
        self.root.bind('<KeyPress>', self.enter_shortcut)

        self.label = tk.Label(self.root, text='First interface designed by O.Lebediev', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10, pady=10)

        self.frame = tk.Frame(self.root, background='white', pady=10)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.button = tk.Button(self.frame, text='Enter data', command=self.enter_data)
        self.button.grid(row=0, column=0, columnspan=3)

        self.root.mainloop()

    def enter_data(self):
        messagebox.showinfo(title='Information', message=f"The message you've entered: {self.entry.get()}")

    # shortcut functionality
    def enter_shortcut(self, event):
        if event.keysym == 'Return' and event.state == 8:
            self.enter_data()


GUI()
