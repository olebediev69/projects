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
    return "Data saved successfully"


def duplicate_check(name):
    global col_df
    return name not in col_df['Name'].values


class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Application')
        self.geometry('800x800')

        # Load lists from DataFrame
        self.locations_list = [str(i) for i in ranges_df['Locations'].unique()]
        self.areas_list = [str(i) for i in ranges_df['Areas'].unique()]
        self.prices_list = [str(i) for i in ranges_df['Prices'].unique()]

        # Button to add a new coliving
        self.add_col_button = ctk.CTkButton(
            master=self,
            text='Add Coliving',
            command=self.open_add_window
        )
        self.add_col_button.pack(pady=20)

        # List Panel for displaying colivings
        self.list_panel = ctk.CTkFrame(self)
        self.list_panel.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.refresh_col_list()

    def refresh_col_list(self):
        for widget in self.list_panel.winfo_children():
            widget.destroy()

        for index, row in col_df.iterrows():
            frame = ctk.CTkFrame(self.list_panel)
            frame.pack(fill=tk.X, padx=10, pady=5)

            ctk.CTkLabel(frame, text=row['Name']).pack(side=tk.LEFT, padx=10)
            ctk.CTkLabel(frame, text=row['Location']).pack(side=tk.LEFT, padx=10)
            ctk.CTkLabel(frame, text=row['Area']).pack(side=tk.LEFT, padx=10)
            ctk.CTkLabel(frame, text=row['State']).pack(side=tk.LEFT, padx=10)
            ctk.CTkLabel(frame, text=row['Price']).pack(side=tk.LEFT, padx=10)

    def open_add_window(self):
        if not hasattr(self, 'add_window') or not self.add_window.winfo_exists():
            self.add_window = AddWindow(self)
        self.add_window.focus_set()


class AddWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Add Coliving")
        self.geometry("400x300")
        self.master = master

        self.setup_ui()

    def setup_ui(self):
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name")
        self.name_entry.pack(pady=10)

        self.location_entry = ctk.CTkEntry(self, placeholder_text="Location")
        self.location_entry.pack(pady=10)

        self.area_entry = ctk.CTkEntry(self, placeholder_text="Area (m^2)")
        self.area_entry.pack(pady=10)

        self.state_menu = ctk.CTkOptionMenu(self, values=["Excellent", "Good", "Normal", "Bad"])
        self.state_menu.pack(pady=10)

        self.price_entry = ctk.CTkEntry(self, placeholder_text="Price ($/month)")
        self.price_entry.pack(pady=10)

        submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_data)
        submit_button.pack(pady=20)

    def submit_data(self):
        name = self.name_entry.get()
        location = self.location_entry.get()
        area = self.area_entry.get()
        state = self.state_menu.get()
        price = self.price_entry.get()

        result = save_data(name, location, area, state, price)
        if result == "Duplicate entry exists":
            ctk.CTkLabel(self, text=result).pack()
        else:
            self.master.refresh_col_list()
            self.destroy()


if __name__ == '__main__':
    app = AppWindow()
    app.mainloop()
