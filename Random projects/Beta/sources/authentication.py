import tkinter as tk
import customtkinter as ctk
import pandas as pd
from tkinter import messagebox

# set the default appearance
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

data_df = pd.read_csv('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/data.csv')
DATA_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/data.csv'


def reload_df(path):
    global data_df
    data_df = pd.read_csv(path)
    return data_df


def add_data(login, password):
    global data_df
    new_info = pd.DataFrame([{'Login': login, 'Password': password}])
    if not duplicate_check(login):
        return "Duplicate entry exists"
    new_info_df = pd.concat([data_df, new_info], ignore_index=True)
    new_info_df.to_csv(DATA_PATH, index=False)
    reload_df(DATA_PATH)


def duplicate_check(login):
    global data_df
    return login not in data_df['Login'].values


class RegistrationWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Registration')
        self.geometry('400x380')
        self.resizable(True, False)

        # registration label
        self.label = ctk.CTkLabel(
            master=self,
            text='Registration',
            font=('Calibri', 40, 'bold')
        )
        self.label.pack(
            padx=10,
            pady=(30, 0)
        )

        # data fields
        self.login_entry = ctk.CTkEntry(
            master=self,
            height=50,
            placeholder_text='Login',
        )
        self.login_entry.pack(
            padx=50,
            pady=(30, 0),
            fill=tk.X,
        )

        self.password_entry = ctk.CTkEntry(
            master=self,
            height=50,
            placeholder_text='Password',
            show='*',
        )
        self.password_entry.pack(
            padx=50,
            pady=(5, 10),
            fill=tk.X,
        )

        # errors field
        self.error_field = ctk.CTkLabel(
            master=self,
            text='',
            font=('Calibri', 15, 'italic'),
        )
        self.error_field.pack()

        # show password checkbox
        self.checkbox_var = tk.StringVar(value='off')
        self.checkbox = ctk.CTkCheckBox(
            master=self,
            text='Show password',
            variable=self.checkbox_var,
            onvalue='on',
            offvalue='off',
            command=self.show_password,
            corner_radius=20,
            checkbox_width=30,
            checkbox_height=30,
            border_width=1,
            font=('Calibri', 10),
        )
        self.checkbox.pack(
            padx=10,
            pady=20,
        )

        # functionality
        self.go_button = ctk.CTkButton(
            master=self,
            text='Go',
            command=self.proceed_registration,
            height=40,
        )
        self.go_button.pack(
            fill=tk.X,
            padx=50,
        )

    def info_message(self, message, color):
        self.error_field.configure(text=message, text_color=color)
        self.update_idletasks()

    def proceed_registration(self):
        reload_df(DATA_PATH)
        confirmation = messagebox.askquestion('Are you sure?', 'Are you sure you want to register this account?')
        if confirmation == 'yes':
            login = self.login_entry.get()
            password = self.password_entry.get()
            if duplicate_check(login):
                message = add_data(login, password)
                if message:
                    self.info_message(message, 'red')
                else:
                    self.after(500, lambda: self.info_message('Registration successful!', 'green'))
                    self.after(1500, lambda: self.info_message('Quitting...', 'black'))
                    self.after(3000, self.destroy)
            else:
                self.info_message('Profile already exists', 'red')

    def show_password(self):
        if self.checkbox_var.get() == 'on':
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login Window')
        self.geometry('400x420')
        self.resizable(True, False)

        # login label
        self.label = ctk.CTkLabel(
            master=self,
            text='Login',
            font=('Calibri', 40, 'bold')
        )
        self.label.pack(
            padx=10,
            pady=(30, 0)
        )

        # data fields
        self.login_entry = ctk.CTkEntry(
            master=self,
            height=50,
            placeholder_text='Login',
        )
        self.login_entry.pack(
            padx=50,
            pady=(30, 0),
            fill=tk.X,
        )

        self.password_entry = ctk.CTkEntry(
            master=self,
            height=50,
            placeholder_text='Password',
            show='*',
        )
        self.password_entry.pack(
            padx=50,
            pady=(5, 10),
            fill=tk.X,
        )

        # errors field
        self.error_field = ctk.CTkLabel(
            master=self,
            text='',
            font=('Calibri', 15, 'italic'),
        )
        self.error_field.pack()

        # show password checkbox
        self.checkbox_var = tk.StringVar(value='off')
        self.checkbox = ctk.CTkCheckBox(
            master=self,
            text='Show password',
            variable=self.checkbox_var,
            onvalue='on',
            offvalue='off',
            command=self.show_password,
            corner_radius=20,
            checkbox_width=30,
            checkbox_height=30,
            border_width=1,
            font=('Calibri', 10),
        )
        self.checkbox.pack(
            padx=10,
            pady=20,
        )

        # functionality
        self.go_button = ctk.CTkButton(
            master=self,
            text='Go',
            command=self.proceed_login,
            height=40,
        )
        self.go_button.pack(
            fill=tk.X,
            padx=50,
        )

        # registration field
        self.registration_label = ctk.CTkButton(
            master=self,
            text="Don't have an account?",
            font=('Calibri', 10),
            height=10,
            command=self.registration,
            fg_color='darkcyan'
        )
        self.registration_label.pack(
            padx=10,
            pady=(10, 0)
        )

        self.registration_window = None

        self.mainloop()

    def info_message(self, message, color):
        self.error_field.configure(text=message, text_color=color)
        self.update_idletasks()

    def proceed_login(self):
        if self.login_entry.get().strip() == '' or self.password_entry.get().strip() == '':
            self.error_field.configure(text="You haven't entered some data", text_color='red')
        else:
            login = self.login_entry.get().strip()
            password = self.password_entry.get().strip()
            if login in data_df['Login'].values:
                actual_password = data_df.loc[data_df['Login'] == login, 'Password'].values[0]
                if password == actual_password:
                    self.after(500, lambda: self.info_message('Login successful', 'green'))
                    self.after(1500, lambda: self.info_message('Quitting...', 'black'))
                    self.after(3000, self.destroy)
                    return True
                else:
                    self.error_field.configure(text="You have entered wrong data", text_color='red')
            else:
                self.error_field.configure(text="You have entered wrong data", text_color='red')

    def show_password(self):
        if self.checkbox_var.get() == 'on':
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')

    def registration(self):
        if self.registration_window is None or not self.registration_window.winfo_exists():
            self.registration_window = RegistrationWindow()
        else:
            self.registration_window.focus()


if __name__ == '__main__':
    LoginWindow()
