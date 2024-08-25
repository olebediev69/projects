import customtkinter as ctk
import tkinter as tk
import pandas as pd

COL_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/colivings.csv'
col_df = pd.read_csv(COL_PATH)
RANGES_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/ranges.csv'
ranges_df = pd.read_csv(RANGES_PATH)


def reload_col(path):
    global col_df
    col_df = pd.read_csv(path)
    return col_df


def reload_ranges(path):
    global ranges_df
    ranges_df = pd.read_csv(path)
    return ranges_df


def save_data(name, location, area, state, price):
    global col_df
    if not duplicate_check(name):
        return "Duplicate entry exists"

    new_info_col = pd.DataFrame([{
        'Name': name,
        'Location': location,
        'Area': f'{area} m^2',
        'State': state,
        'Price': f'${price}/month',
    }])
    new_info_col_df = pd.concat([col_df, new_info_col], ignore_index=True)
    new_info_col_df.to_csv(COL_PATH, index=False)

    new_info_ranges = pd.DataFrame([{
        'Locations': location,
        'Areas': f'{area} m^2',
        'Prices': f'${price}/month',
    }])
    new_info_ranges_df = pd.concat([ranges_df, new_info_ranges], ignore_index=True)
    new_info_ranges_df.to_csv(RANGES_PATH, index=False)

    reload_col(COL_PATH)
    reload_ranges(RANGES_PATH)


def duplicate_check(name):
    global col_df
    return name not in col_df['Name'].values


class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.list_option_frame = None
        self.title('Application')
        self.geometry('800x800')

        # lists for available options
        self.locations_list = [str(i) for i in ranges_df['Locations'].to_list()]
        self.areas_list = [str(i) for i in ranges_df['Areas'].to_list()]
        self.prices_list = [str(i) for i in ranges_df['Prices'].to_list()]

        self.create_ui()
        self.refresh_col_list()

        self.add_window = None

        self.mainloop()

    def create_ui(self):
        # hosts panel
        self.hosts_panel = ctk.CTkFrame(
            master=self,
            height=40,
        )
        self.hosts_panel.pack(
            fill=tk.X,
            anchor='n',
            padx=10,
            pady=(10, 0),
        )

        self.add_col = ctk.CTkButton(
            master=self.hosts_panel,
            text='+',
            width=15,
            height=15,
            command=self.add_col,
        )
        self.add_col.pack(
            padx=(10, 5),
            pady=5,
            anchor='w',
        )

        # filters panel
        self.filters_panel = ctk.CTkFrame(
            master=self,
            height=40,
        )
        self.filters_panel.pack(
            fill=tk.X,
            anchor='n',
            pady=5,
            padx=10,
        )

        self.filters_label = ctk.CTkLabel(
            master=self.filters_panel,
            text="Filters:",
            font=("Calibri", 20, 'bold'),
        )
        self.filters_label.pack(
            side=tk.LEFT,
            padx=10,
            pady=10,
        )

        self.state_var = tk.StringVar(value="State")
        self.state = ctk.CTkOptionMenu(
            master=self.filters_panel,
            values=['Excellent', 'Good', 'Normal', 'Bad'],
            variable=self.state_var,
            font=("Calibri", 15),
        )

        self.area_var = ctk.StringVar(value="Area")
        self.area = ctk.CTkOptionMenu(
            master=self.filters_panel,
            values=self.areas_list,
            variable=self.area_var,
            font=("Calibri", 15),
        )
        self.area.pack(
            side=tk.RIGHT,
            padx=(0, 5),
        )

        self.location_var = tk.StringVar(value="Location")
        self.location = ctk.CTkOptionMenu(
            master=self.filters_panel,
            values=self.locations_list,
            font=("Calibri", 15),
            variable=self.location_var,
        )
        self.location.pack(
            side=tk.RIGHT,
            padx=(0, 5),
        )

        self.name = ctk.CTkEntry(
            master=self.filters_panel,
            placeholder_text="Name",
            font=("Calibri", 15),
        )
        self.name.pack(
            side=tk.RIGHT,
            padx=(0, 5),
        )

        # col list
        self.col_list = ctk.CTkFrame(
            master=self,
        )
        self.col_list.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=(0, 30),
        )

    def add_col(self):
        if self.add_window is None or not self.add_window.winfo_exists():
            self.add_window = AddWindow(self)
        else:
            self.add_window.focus()

    def refresh_col_list(self):

        def divider(master):
            div = ctk.CTkLabel(
                master=master,
                font=("Calibri", 13, "bold"),
                text='|'
            )
            div.pack(
                side=tk.RIGHT,
                padx=10
            )

        for widget in self.col_list.winfo_children():
            widget.destroy()

        for i in range(0, len(col_df)):
            frame = ctk.CTkFrame(
                master=self.col_list,
                fg_color='darkcyan',
            )
            frame.pack(
                fill=tk.X,
                anchor='n',
                padx=10,
                pady=(10, 0),
            )
            name = ctk.CTkLabel(
                master=frame,
                text=col_df['Name'].values[i],
                font=("Calibri", 13),
            )
            name.pack(
                side=tk.LEFT,
                padx=10,
                pady=10,
            )

            price = ctk.CTkLabel(
                master=frame,
                text=col_df['Price'].values[i],
                font=("Calibri", 13),
            )
            price.pack(
                side=tk.RIGHT,
                padx=10,
                pady=10,
            )

            divider(frame)

            state = ctk.CTkLabel(
                master=frame,
                text=col_df['State'].values[i],
                font=("Calibri", 13),
            )
            state.pack(
                side=tk.RIGHT,
                padx=10,
                pady=10,
            )

            divider(frame)

            area = ctk.CTkLabel(
                master=frame,
                text=col_df['Area'].values[i],
                font=("Calibri", 13),
            )
            area.pack(
                side=tk.RIGHT,
                padx=10,
                pady=10,
            )

            divider(frame)

            location = ctk.CTkLabel(
                master=frame,
                text=col_df['Location'].values[i],
                font=("Calibri", 13),
            )
            location.pack(
                side=tk.RIGHT,
                padx=10,
                pady=10,
            )
        self.update_idletasks()


class AddWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("New Coliving")
        self.geometry("400x300")
        self.resizable(False, False)

        self.bind('<KeyPress>', self.auto_data_fill)

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

        self.name_var = tk.StringVar(value="")
        self.name = ctk.CTkEntry(
            master=self.name_frame,
            font=("Calibri", 15),
            textvariable=self.name_var,
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

        self.location_var = tk.StringVar(value="")
        self.location = ctk.CTkEntry(
            master=self.location_frame,
            font=("Calibri", 15),
            textvariable=self.location_var,
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

        self.area_var = tk.StringVar(value="")
        self.area = ctk.CTkEntry(
            master=self.area_frame,
            font=("Calibri", 15),
            textvariable=self.area_var,
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

        self.price_var = tk.StringVar(value="")
        self.price = ctk.CTkEntry(
            master=self.price_frame,
            font=("Calibri", 15),
            textvariable=self.price_var,
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
                    self.master.refresh_col_list()

    def auto_data_fill(self, event):
        if event.char == '=' and event.state == 8:
            self.name_var.set('Trap Xata')
            self.location_var.set('Lesi Ukrainky 30B')
            self.area_var.set('440')
            self.state.set('Excellent')
            self.price_var.set('40000')


if __name__ == '__main__':
    app = AppWindow()
    app.mainloop()
