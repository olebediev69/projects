import tkinter as tk
import customtkinter as ctk
import pandas as pd
import warnings

warnings.filterwarnings("ignore", message="Exception in Tkinter callback")

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


class HostsApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # default settings
        self.title("New studliving")
        self.geometry('500x420')
        self.resizable(True, False)

        # pandas-necessary variables
        self.COLIVINGS_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/colivings.csv'
        self.colivings_df = pd.read_csv(self.COLIVINGS_PATH)
        self.RANGES_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/ranges.csv'
        self.ranges_df = pd.read_csv(self.RANGES_PATH)

        # announcements for the widgets initialization
        self.header_panel = None
        self.header_label = None

        self.body_panel = None
        self.label = None
        self.name_var = None
        self.name = None
        self.location_var = None
        self.location = None
        self.area_var = None
        self.area = None
        self.state_var = None
        self.state = None
        self.price_var = None
        self.price = None
        self.info_field = None
        self.add_button = None

        # adding widgets to main screen
        self.header_initialization()
        self.body_initialization()

        # main loop of the program
        # self.mainloop()

    def header_initialization(self):
        print()
        print('# Header debug message')

        self.header_panel = ctk.CTkFrame(
            master=self,
            height=80,
        )
        self.header_panel.pack(fill=tk.X,)
        print('\t• Header panel - ✓')

        self.header_label = ctk.CTkLabel(
            master=self.header_panel,
            text='Studliving form:',
            font=('Calibri', 30, 'bold', 'italic'),
        )
        self.header_label.pack(pady=10,)
        print('\t• Header label - ✓')

        print()
        print('-' * 50)

    def body_initialization(self):
        print()
        print('# Body debug message')

        # body panel
        self.body_panel = ctk.CTkFrame(
            master=self,
        )
        self.body_panel.pack(fill=tk.BOTH, expand=True, pady=(3, 0))
        print('\t• Body panel - ✓')

        # body grid configuration
        self.body_panel.columnconfigure(0, weight=0)
        self.body_panel.columnconfigure(1, weight=1)

        # body widgets' variables
        self.name_var = tk.StringVar(value='')
        self.location_var = tk.StringVar(value='')
        self.area_var = tk.StringVar(value='')
        self.state_var = tk.StringVar(value='Not selected')
        self.price_var = tk.StringVar(value='')

        # body widgets' labels initialization
        labels_list = ['• Name:',
                       '• Location:',
                       '• Area (m^2):',
                       '• State:',
                       '• Price ($/month):']
        for label in labels_list:
            self.label = ctk.CTkLabel(
                master=self.body_panel,
                text=label,
                font=('Calibri', 20),
            )
            self.label.grid(column=0, row=labels_list.index(label), pady=(20, 0), padx=(20, 0), sticky='wns')
        print('\t• Body labels - ✓')

        print()

        # body widgets' entries initialization
        self.name = ctk.CTkEntry(
            master=self.body_panel,
            textvariable=self.name_var,
            font=('Calibri', 20),
        )
        self.name.grid(column=1, row=0, sticky='ew', pady=(20, 0), padx=(0, 20))
        print('\t• Name entry - ✓')

        self.location = ctk.CTkEntry(
            master=self.body_panel,
            textvariable=self.location_var,
            font=('Calibri', 20),
        )
        self.location.grid(column=1, row=1, sticky='ew', pady=(20, 0), padx=(20, 20))
        print('\t• Location entry - ✓')

        self.area = ctk.CTkEntry(
            master=self.body_panel,
            textvariable=self.area_var,
            font=('Calibri', 20),
        )
        self.area.grid(column=1, row=2, sticky='ew', pady=(20, 0), padx=(20, 20))
        print('\t• Area entry - ✓')

        self.state = ctk.CTkOptionMenu(
            master=self.body_panel,
            variable=self.state_var,
            values=['Not selected', 'Excellent', 'Good', 'Medium'],
            font=('Calibri', 20),
            fg_color='darkgray',
            text_color='black',
            button_color='darkgray',
            button_hover_color='gray',
        )
        self.state.grid(column=1, row=3, sticky='ew', pady=(20, 0), padx=(20, 20))
        print('\t• State entry - ✓')

        self.price = ctk.CTkEntry(
            master=self.body_panel,
            textvariable=self.price_var,
            font=('Calibri', 20),
        )
        self.price.grid(column=1, row=4, sticky='ew', pady=(20, 0), padx=(20, 20))
        print('\t• Price entry - ✓')

        self.info_field = ctk.CTkLabel(
            master=self.body_panel,
            font=('Calibri', 15),
            text='',
        )
        self.info_field.grid(row=5, sticky='ew', pady=(10, 0), columnspan=2,)
        print('\t• Info field - ✓')

        self.add_button = ctk.CTkButton(
            master=self.body_panel,
            text='ADD STUDLIVING',
            font=('Calibri', 20, 'bold'),
            command=self.add_studliving,
            fg_color='gray',
            hover_color='darkgray',
            text_color='black',
        )
        self.add_button.grid(row=6, sticky='ew', pady=(10, 20), padx=(20, 20), columnspan=2)
        print('\t• Add button - ✓')

        print()
        print('-' * 50)

    # buttons/info-related functions
    def add_studliving(self):
        self.add_button.configure(state='disabled')
        name = self.name.get()
        location = self.location.get()
        area = self.area.get()
        state = self.state.get()
        price = self.price.get()

        self.save_data_to_csv(name, location, area, state, price)

        self.parent.refresh_ui()

        print()
        print("# Add studliving button's pressed")
        print()
        print('-' * 50)

        print(self.colivings_df)

    def display_information(self, message, color):
        self.info_field.configure(text=message, text_color=color)

    # pandas-related functions
    def reload_pandas(self):
        self.colivings_df = pd.read_csv(self.COLIVINGS_PATH)
        self.ranges_df = pd.read_csv(self.RANGES_PATH)

    def info_validation(self, name, area, state, price):
        self.colivings_df = pd.read_csv(self.COLIVINGS_PATH)
        check_list = [name, area, state, price]

        if not all(check_list):
            self.display_information('You have some empty blanks.', color='red')
        else:
            if name not in [str(i) for i in self.colivings_df['Name']]:
                if (not area.isnumeric()) or (not price.isnumeric()):
                    self.display_information('Area and price must be positive integers or floats.', color='red')
                else:
                    if state == 'Not selected':
                        self.display_information('You have not selected a state.', color='red')
                    else:
                        return True
            else:
                self.display_information('The studliving already exists.', color='red')

    def save_data_to_csv(self, name, location, area, state, price):
        duplicates = self.info_validation(name, area, state, price)
        if duplicates:
            new_data_colivings_df = pd.DataFrame([{'Name': name, 'Location': location, 'Area': area, 'State': state, 'Price': price}])
            new_data_colivings_df = pd.concat([new_data_colivings_df, self.colivings_df], ignore_index=True)
            new_data_colivings_df.to_csv(self.COLIVINGS_PATH, index=False)

            new_data_ranges_df = pd.DataFrame([{'Locations': location, 'Areas': area, 'Prices': price}])
            new_data_ranges_df = pd.concat([new_data_ranges_df, self.ranges_df], ignore_index=True)
            new_data_ranges_df.to_csv(self.RANGES_PATH, index=False)
            self.reload_pandas()
            self.display_information('Data saved.', color='green')
            self.after(1000, self.destroy)