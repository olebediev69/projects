import tkinter as tk
import customtkinter


class Calculator:
    def __init__(self):
        self.button = None
        self.master = tk.Tk()
        self.master.geometry('500x550')
        self.master.title('Calculator')
        self.master.resizable(False, False)

        self.result_frame = customtkinter.CTkFrame(
            master=self.master,
            fg_color='gray'
        )
        self.result_frame.pack(
            fill=tk.BOTH,
            pady=(30,10)
        )

        self.result = customtkinter.CTkLabel(
            master=self.result_frame,
            text='...',
            font=('Calibri', 30)
        )
        self.result.pack(
            pady=10
        )

        self.buttons_frame = customtkinter.CTkFrame(
            master=self.master
        )
        self.buttons_frame.pack(
            fill=tk.BOTH,
            expand=True,
            pady=10
        )

        self.create_buttons()

        self.master.mainloop()

    def create_buttons(self):
        for i in range(15):
            for row in range(3):
                for col in range(3):
                    self.button = customtkinter.CTkButton(
                        master=self.buttons_frame,
                        text=f'{i}'
                    )
                    self.button.grid(
                        row=row,
                        column=col,
                        padx=2,
                        pady=2
                    )


if __name__ == '__main__':
    Calculator()