import customtkinter as ctk
import tkinter as tk
import pandas as pd

COL_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/colivings.csv'
col_df = pd.read_csv(COL_PATH)
RANGES_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/ranges.csv'
ranges_df = pd.read_csv(RANGES_PATH)
PRESET_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/preset.csv'
PRESET2_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/preset(2).csv'

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

        # menu
        self.menu = tk.Menu(self)
        self.configure(menu=self.menu)
        self.options_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Options', menu=self.options_menu)
        self.options_menu.add_command(label='Reset filters', command=self.reset_filters)
        self.options_menu.add_command(label='Clear colivings list', command=self.clear_col_list)
        self.options_menu.add_command(label='Upload coliving data', command=self.upload_col_info)

        self.price_var = tk.StringVar(value="Price")
        self.state_var = tk.StringVar(value="State")

        reload_col(COL_PATH)
        reload_ranges(RANGES_PATH)

        # lists for available options
        self.locations_list = [str(i) for i in ranges_df['Locations'].to_list()]
        self.areas_list = [str(i) for i in ranges_df['Areas'].to_list()]
        self.prices_list = [str(i) for i in ranges_df['Prices'].to_list()]

        self.create_ui()
        self.refresh_col_list()
        self.refresh_ui()

        self.add_window = None

        self.mainloop()

    def upload_col_info(self):
        global col_df, ranges_df
        data_df = pd.read_csv(PRESET_PATH)
        col_df = pd.concat([data_df, col_df], ignore_index=True)
        col_df.to_csv(COL_PATH, index=False)

        data1_df = pd.read_csv(PRESET2_PATH)
        ranges_df = pd.concat([ranges_df, data1_df], ignore_index=True)
        ranges_df.to_csv(RANGES_PATH, index=False)

        reload_col(COL_PATH)
        self.refresh_ui()

    def reset_filters(self):
        self.name.delete(0, tk.END)
        self.name.configure(placeholder_text='Name')
        self.location.set('Location')
        self.area.configure(to=max(self.int_areas_list) if self.int_areas_list else 100)
        self.area_var.set(0)
        self.state_var.set('State')
        self.price_var.set('Price')
        self.update_options()

    def clear_col_list(self):
        global col_df, ranges_df
        col_df = pd.DataFrame(columns=col_df.columns)
        ranges_df = pd.DataFrame(columns=ranges_df.columns)

        col_df.to_csv(COL_PATH, index=False)
        ranges_df.to_csv(RANGES_PATH, index=False)

        self.refresh_ui()

    def update_options(self):
        self.locations_list = [str(i) for i in col_df['Location'].unique()]
        self.areas_list = [str(i) for i in col_df['Area'].unique()]
        self.prices_list = [str(i) for i in col_df['Price'].unique()]

        self.location['values'] = self.locations_list
        self.price['values'] = self.prices_list

        self.int_areas_list = [int(i.split()[0]) for i in self.areas_list if i.split()[0].isdigit()]
        max_area = max(self.int_areas_list) if self.int_areas_list else 100
        self.area.configure(to=max_area)

        self.area_display.configure(text=f'Area: {self.area.get()} m^2')
        self.refresh_col_list()

    def refresh_ui(self):
        self.update_options()
        self.apply_filters_button.invoke()

    def create_ui(self):
        ###
        self.price_var.set("Price")
        self.state_var.set("State")

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

        ###
        # filters panel
        self.int_areas_list = [int(i.split()[0]) for i in self.areas_list]
        self.int_prices_list = [int(i.split('/')[0][1:]) for i in self.prices_list]

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

        self.price_var = tk.StringVar(value="Price")
        self.price = ctk.CTkOptionMenu(
            master=self.filters_panel,
            variable=self.price_var,
            values=self.prices_list,
            font=("Calibri", 15),
            width=10,
        )
        self.price.pack(
            side=tk.RIGHT,
            padx=(0, 5),
        )

        self.state_var = tk.StringVar(value="State")
        self.state = ctk.CTkOptionMenu(
            master=self.filters_panel,
            values=['Excellent', 'Good', 'Normal', 'Bad'],
            variable=self.state_var,
            font=("Calibri", 15),
            width=10,
        )
        self.state.pack(
            side=tk.RIGHT,
            padx=(0, 5),
        )

        self.area_var = tk.IntVar(value=0)
        self.area = ctk.CTkSlider(
            master=self.filters_panel,
            width=80,
            from_=0,
            command=self.update_area_display,
            variable=self.area_var,
        )
        self.area.pack(
            side=tk.RIGHT,
            padx=(0, 5),
        )
        self.area_display = ctk.CTkLabel(
            master=self.filters_panel,
            text=f'Area: {self.area.get()} m^2',
            font=("Calibri", 15),
        )
        self.area_display.pack(
            side=tk.RIGHT,
            padx=(0, 5),
        )

        self.location_var = tk.StringVar(value="Location")
        self.location = ctk.CTkOptionMenu(
            master=self.filters_panel,
            values=self.locations_list,
            font=("Calibri", 15),
            variable=self.location_var,
            width=10,
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

        ###
        # apply filters button
        self.apply_filters_button = ctk.CTkButton(
            master=self,
            text='Apply Filters',
            font=("Calibri", 15, 'bold'),
            corner_radius=20,
            command=self.apply_filters
        )
        self.apply_filters_button.pack(
            fill=tk.X,
            padx=250,
            pady=10,
        )

        ###
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

    def apply_filters(self):
        print('Filters debug message:')
        print(f'Name: {self.name.get() if self.name.get() else None}')
        print(f'Area: {self.area.get()}')
        print(f'State: {self.state.get()}')
        print(f'Price: {self.price.get()}')
        self.refresh_col_list()

    def update_area_display(self, value):
        self.area_display.configure(text=f'Area: {int(value)} m^2')

    def add_col(self):
        if self.add_window is None or not self.add_window.winfo_exists():
            self.add_window = AddWindow(self)
        else:
            self.add_window.focus()

    def refresh_col_list(self):
        print("Refreshing col list...")
        conditions = pd.Series([True] * len(col_df))

        self.apply_condition_filters(conditions)

        filtered_df = col_df[conditions]
        print(f"Filtered entries: {len(filtered_df)}")
        print(filtered_df.head())  # Print first few rows to verify

        self.populate_col_list(filtered_df)

    def apply_condition_filters(self, conditions):
        filter_name = self.name.get()
        filter_area = self.area.get()
        filter_state = self.state_var.get()
        filter_price = self.price_var.get()

        if filter_name:
            conditions &= col_df['Name'].str.contains(filter_name, case=False, na=False)
        if filter_area != 0:
            filter_area_str = f"{filter_area} m^2"
            conditions &= col_df['Area'] == filter_area_str
        if filter_state != "State":
            conditions &= col_df['State'] == filter_state
        if filter_price != "Price":
            price_num = int(filter_price.replace('$', '').split('/')[0])
            filter_price_str = f"${price_num}/month"
            conditions &= col_df['Price'] == filter_price_str

    def populate_col_list(self, df):
        for widget in self.col_list.winfo_children():
            widget.destroy()

        for i, row in df.iterrows():
            frame = ctk.CTkFrame(master=self.col_list, fg_color='darkcyan')
            frame.pack(fill=tk.X, anchor='n', padx=10, pady=(10, 0))

            for col in ['Name', 'Location', 'Area', 'State', 'Price']:
                label = ctk.CTkLabel(master=frame, text=f"{col}: {row[col]}", font=("Calibri", 13))
                label.pack(side=tk.LEFT, padx=10, pady=10, expand=True)


class AddWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("New Coliving")
        self.geometry("400x300")
        self.resizable(False, False)

        self.init_widgets()
        self.init_filters()

        self.bind('<KeyPress>', self.auto_data_fill)

    def init_widgets(self):
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

    def init_filters(self):
        self.name.set('')
        self.area.set('0')
        self.state.set('Select State')
        self.price.set('0')

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
        print("Key Pressed:", event.char, event.keysym, event.keycode)
        if event.char == '=' and event.state == 8:
            self.name_var.set('Trap Xata')
            self.location_var.set('Lesi Ukrainky 30B')
            self.area_var.set('440')
            self.state.set('Excellent')
            self.price_var.set('40000')
        self.name.update()
        self.location.update()
        self.area.update()
        self.state.update()
        self.price.update()


if __name__ == '__main__':
    app = AppWindow()
    app.mainloop()
