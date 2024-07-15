import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

class App:
    def __init__(self):
        self.root = customtkinter.CTk()

        self.root.geometry('300x200')
        self.root.resizable(False, False)
        self.root.title('Three Buttons Example')

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20)

        self.button1 = customtkinter.CTkButton(
            master=self.frame, font=('Arial', 18), text='Click me 1',
            command=lambda: self.button_clicked(self.button1)
        )
        self.button1.grid(row=0, column=0, padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(
            master=self.frame, font=('Arial', 18), text='Click me 2',
             command=lambda: self.button_clicked(self.button2)
        )
        self.button2.grid(row=0, column=1, padx=10, pady=10)

        self.button3 = customtkinter.CTkButton(
            master=self.frame, font=('Arial', 18), text='Click me 3',
            command=lambda: self.button_clicked(self.button3)
        )
        self.button3.grid(row=0, column=2, padx=10, pady=10)

        self.root.mainloop()

    def button_clicked(self, button):
        button.configure(text='X')

App()
