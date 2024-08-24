import customtkinter as ctk
import tkinter as tk
import pandas as pd

COL_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/colivings.csv'
col_df = pd.read_csv(COL_PATH)


def reload_df(path):
    global col_df
    col_df = pd.read_csv(path)
    return col_df


def save_data(name, location, area, state, price):
    global col_df
    if not duplicate_check(name):
        return "Duplicate entry exists"
    new_info = pd.DataFrame([{'Name': name, 'Location': location, 'Area': area, 'State': state, 'Price': price}])
    new_info_df = pd.concat([col_df, new_info], ignore_index=True)
    new_info_df.to_csv(COL_PATH, index=False)
    reload_df(COL_PATH)

def duplicate_check(name):
    global col_df
    return name not in col_df['Name'].values


class AddWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("New Coliving")
        self.geometry("400x300")
        self.resizable(False, False)

        self.name_frame = ctk.CTkFrame(self)
        self.name_frame.pack(padx=20, pady=(30, 5), fill=tk.X)

        self.name_label = ctk.CTkLabel(
            master=self.name_frame,
            text="Name:",
            font=("Calibri", 15),
            width=80,
            anchor="w"
        )
        self.name_label.pack(side=tk.LEFT)

        self.name = ctk.CTkEntry(
            master=self.name_frame,
            placeholder_text="Name",
            font=("Calibri", 15),
        )
        self.name.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.location_frame = ctk.CTkFrame(self)
        self.location_frame.pack(padx=20, pady=(0, 5), fill=tk.X)

        self.location_label = ctk.CTkLabel(
            master=self.location_frame,
            text="Location:",
            font=("Calibri", 15),
            width=80,
            anchor="w"
        )
        self.location_label.pack(side=tk.LEFT)

        self.location = ctk.CTkEntry(
            master=self.location_frame,
            placeholder_text="Location",
            font=("Calibri", 15),
        )
        self.location.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.area_frame = ctk.CTkFrame(self)
        self.area_frame.pack(padx=20, pady=(0, 5), fill=tk.X)

        self.area_label = ctk.CTkLabel(
            master=self.area_frame,
            text="Area:",
            font=("Calibri", 15),
            width=80,
            anchor="w"
        )
        self.area_label.pack(side=tk.LEFT)

        self.area = ctk.CTkEntry(
            master=self.area_frame,
            placeholder_text="Area",
            font=("Calibri", 15),
        )
        self.area.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.state_frame = ctk.CTkFrame(self)
        self.state_frame.pack(padx=20, pady=(0, 5), fill=tk.X)

        self.state_label = ctk.CTkLabel(
            master=self.state_frame,
            text="State:",
            font=("Calibri", 15),
            width=80,
            anchor="w"
        )
        self.state_label.pack(side=tk.LEFT)

        self.state_var = tk.StringVar(value="")
        self.state = ctk.CTkOptionMenu(
            master=self.state_frame,
            values=['Excellent', 'Good', 'Normal', 'Bad'],
            variable=self.state_var,
        )
        self.state.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.price_frame = ctk.CTkFrame(self)
        self.price_frame.pack(padx=20, pady=(0, 5), fill=tk.X)

        self.price_label = ctk.CTkLabel(
            master=self.price_frame,
            text="Price:",
            font=("Calibri", 15),
            width=80,
            anchor="w"
        )
        self.price_label.pack(side=tk.LEFT)

        self.price = ctk.CTkEntry(
            master=self.price_frame,
            placeholder_text="Price",
            font=("Calibri", 15),
        )
        self.price.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.info = ctk.CTkLabel(
            master=self,
            text='',
            font=("Calibri", 10, "italic")
        )
        self.info.pack()

        self.go_button = ctk.CTkButton(
            master=self,
            text='Add Coliving',
            font=('Calibri', 15),
            fg_color='darkgreen',
            hover_color='green',
            command=self.go_button,
        )
        self.go_button.pack(
            padx=20,
            pady=(15, 10),
            fill=tk.X,
        )

    def info_display(self, text, color):
        self.info.configure(text=text, text_color=color)
        self.update_idletasks()

    def go_button(self):
        name = self.name.get()
        location = self.location.get()
        area = self.area.get()
        state = self.state.get()
        price = self.price.get()
        if not all([name, location, area, state, price]):
            self.info_display('Every field must be filled', 'red')
        else:
            if not (area.isnumeric() or price.isnumeric()):
                self.info_display('Both area and price values must be integers', 'red')
            else:
                message = save_data(name, location, area, state, price)
                if message == "Duplicate entry exists":
                    self.info_display('Such name is already used', 'red')
                else:
                    self.after(100, lambda: self.info_display('Processing...', 'gray'))
                    self.after(1000, lambda: self.info_display('Done', 'green'))
                    self.after(2000, lambda: self.info_display('Exiting...', 'gray'))
                    self.after(3000, self.destroy)


class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Application')
        self.geometry('800x800')

        self.hosts_panel = ctk.CTkFrame(
            master=self,
            height=40,
        )
        self.hosts_panel.pack(
            fill=tk.X,
            expand=True,
            anchor='n',
        )

        self.add_col = ctk.CTkButton(
            master=self.hosts_panel,
            text='+',
            width=15,
            height=15,
            command=self.add_col,
        )
        self.add_col.pack(
            padx=(10,5),
            pady=5,
            anchor='w',
        )

        self.add_window = None

        self.mainloop()

    def add_col(self):
        if self.add_window is None or not self.add_window.winfo_exists():
            self.add_window = AddWindow()
        else:
            self.add_window.focus()


if __name__ == '__main__':
    AppWindow()
