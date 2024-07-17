import customtkinter
import pandas as pd

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
DATABASE = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/custom tkinker/sources/database.csv'

class Register:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title('Registration')
        self.root.geometry('400x300')
        self.root.resizable(False, False)
        self.root.bind('<KeyPress>', self.shortcut)

        self.df = pd.read_csv(DATABASE)

        self.login_label = customtkinter.CTkLabel(
            self.root,
            text='Register:',
            font=('Helvetica', 30)
        )
        self.login_label.pack(
            padx=10,
            pady=(50, 10)
        )

        self.login_password_frame = customtkinter.CTkFrame(
            self.root
        )
        self.login_password_frame.pack(
            padx=10,
            pady=10
        )

        self.login = customtkinter.CTkEntry(
            self.login_password_frame,
            font=('Helvetica', 15),
            placeholder_text='Username',
            width=200
        )
        self.login.pack(
            padx=10,
            pady=(10, 10)
        )

        self.password = customtkinter.CTkEntry(
            self.login_password_frame,
            font=('Helvetica', 15),
            show='*',
            placeholder_text='Password',
            width=200
        )
        self.password.pack(
            padx=10,
            pady=(0, 5)
        )

        self.error_message_label = customtkinter.CTkLabel(
            self.login_password_frame,
            font=('Helvetica', 12),
            text=''
        )
        self.error_message_label.pack()

        self.accept_button = customtkinter.CTkButton(self.login_password_frame, text='Accept', command=self.accept)
        self.accept_button.pack(padx=10, pady=(5, 10))

        self.root.mainloop()

    def accept(self):
        login = self.login.get()
        password = self.password.get()
        if not login or not password:
            self.error_message_label.configure(text='Enter login and password.', text_color='red')
        elif login in list(self.df['Login']):
            self.error_message_label.configure(text='This account is already registered.', text_color='red')
        elif login not in list(self.df['Login']) and password:
            current_length = len(list(self.df['Login'])) + 1
            self.df.at[current_length, 'Login'] = login
            self.df.at[current_length, 'Password'] = password
            self.df.to_csv(DATABASE, index=False)
            self.error_message_label.configure(text='Registration successful.', text_color='darkcyan')
            self.root.update()
            self.error_message_label.after(1000, self.error_message_label.configure(text='Quiting...', text_color='gray'))
            self.root.update()
            self.root.after(100, self.root.destroy)
            Login()

    def shortcut(self,event):
        if event.keysym == 'Return':
            self.accept()


class Login:
    def __init__(self):
        self.df = pd.read_csv(DATABASE)

        self.root = customtkinter.CTk()
        self.root.title('Login')
        self.root.geometry('400x400')
        self.root.resizable(False, False)
        self.root.bind('<KeyPress>', self.shortcut)

        self.login_label = customtkinter.CTkLabel(
            self.root,
            text='Login in:',
            font=('Helvetica', 30)
        )
        self.login_label.pack(
            padx=10,
            pady=(50, 10)
        )

        self.login_password_frame = customtkinter.CTkFrame(
            self.root
        )
        self.login_password_frame.pack(
            padx=10,
            pady=10
        )

        self.login = customtkinter.CTkEntry(
            self.login_password_frame,
            font=('Helvetica', 15),
            placeholder_text='Username',
            width=200
        )
        self.login.pack(
            padx=10,
            pady=(10, 10)
        )

        self.password = customtkinter.CTkEntry(
            self.login_password_frame,
            font=('Helvetica', 15),
            show='*',
            placeholder_text='Password',
            width=200
        )
        self.password.pack(
            padx=10,
            pady=(0, 10)
        )

        self.show_password_Var = customtkinter.IntVar(value=0)
        self.show_password = customtkinter.CTkCheckBox(
            self.login_password_frame,
            text='Show password',
            command=self.show_password,
            variable=self.show_password_Var,
            offvalue=0,
            onvalue=1
        )
        self.show_password.pack(
            padx=10,
            pady=(10, 10)
        )

        self.error_message_label = customtkinter.CTkLabel(
            self.login_password_frame,
            font=('Helvetica', 12),
            text=''
        )
        self.error_message_label.pack()

        self.accept_button = customtkinter.CTkButton(
            self.login_password_frame,
            text='Accept',
            command=self.accept,
        )
        self.accept_button.pack(
            padx=10,
            pady=(10, 10)
        )

        self.register_button = customtkinter.CTkButton(
            self.login_password_frame,
            text='Register',
            fg_color='transparent',
            font = ('Helvetica', 10),
            hover_color = 'gray',
            command=self.register_button
        )
        self.register_button.pack(
            padx=10,
            pady=(2, 5)
        )

        self.root.mainloop()

    def show_password(self):
        if self.show_password_Var.get():
            self.password.configure(show='')
        else:
            self.password.configure(show='*')

    def accept(self):
        login = self.login.get()
        password = self.password.get()
        user_row = self.df[self.df['Login'] == login]
        if user_row.empty:
            self.error_message_label.configure(text='There is no such account in database.', text_color='red')
        else:
            if user_row.iloc[0]['Password'] != password:
                self.error_message_label.configure(text='Wrong login or password.', text_color='red')
            else:
                self.error_message_label.configure(text='Access granted.', text_color='darkcyan')
                self.root.update()
                self.error_message_label.after(1000, self.error_message_label.configure(text='Quiting...', text_color='gray'))
                self.root.after(100, self.root.destroy)
                return True

    def shortcut(self, event):
        if event.keysym == 'Return':
            self.accept()

    def register_button(self):
        self.error_message_label.after(100, self.error_message_label.configure(text='Quiting...', text_color='gray'))
        self.root.after(100, self.root.destroy)
        Register()


if __name__ == '__main__':
    Login()