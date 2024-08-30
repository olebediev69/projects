import tkinter as tk
import customtkinter as ctk
import pandas as pd
import warnings
from script.upload_studlivings import Script

warnings.filterwarnings("ignore", message="''CTkOptionMenu' object is not callable")

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # default settings
        self.title('Studliving')
        self.geometry('1280x920')
        # pandas-necessary variables

        self.form_frames = []

        # pandas-necessary variables
        self.COLIVINGS_PATH = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/csvs/colivings.csv'
        self.colivings_df = pd.read_csv(self.COLIVINGS_PATH)

        # announcements for the widgets initialization
        self.filters_panel = None
        self.filters_label = None
        self.menu = None
        self.hosts_options = None
        self.scripts_options = None
        self.area_label = None
        self.label = None
        self.name_filter = None
        self.location_filter_var = None
        self.location_filter = None
        self.area_filter_var = None
        self.area_filter = None
        self.state_filter_var = None
        self.state_filter = None
        self.price_filter_var = None
        self.price_filter = None
        self.apply_filters_button = None

        self.options_frame = None

        self.empty_label = None

        self.form_frame = None
        self.name_label = None
        self.form_label = None

        # adding/reloading widgets on the main screen
        self.initialize_menu()
        self.initialize_filter_widgets()
        self.initialize_options_list()
        self.empty_label_initialization()

        self.load_csv_data()

        # TopLevel for add functionality
        self.hosts_add = None

        # main loop of the program
        self.mainloop()

    # Methods block

    # filters initialization
    def initialize_filter_widgets(self):
        print()
        print('# Widgets initialization debug message:')

        # filters panel
        self.filters_panel = ctk.CTkFrame(
            master=self,
            height=80,
        )
        self.filters_panel.pack(fill='x',)
        self.filters_label = ctk.CTkLabel(
            master=self.filters_panel,
            text='Filters',
            font=('Calibri', 25, 'bold'),
        )
        self.filters_label.grid(row=0, column=0, padx=10, pady=10, sticky='ew', columnspan=5,)

        # filters grid configuration
        for i in range(5):
            self.filters_panel.grid_columnconfigure(i, weight=1)

        print('\t• Filters label - ✓')

        # filter variables
        self.area_filter_var = tk.IntVar(value=0)
        self.location_filter_var = tk.StringVar(value='Not selected')
        self.state_filter_var = tk.StringVar(value='Not selected')
        self.price_filter_var = tk.StringVar(value='Not selected')

        # filter labels
        filter_labels = ['Name', 'Location', '', 'State', 'Price']
        for label in filter_labels:
            self.label = ctk.CTkLabel(
                master=self.filters_panel,
                text=label,
                font=('Calibri', 15),
            )
            self.label.grid(row=1, column=filter_labels.index(label), padx=10, pady=(10,0), sticky='ew',)

        self.area_label = ctk.CTkLabel(
            master=self.filters_panel,
            text=f'Area: {self.area_filter_var.get()}',
            font=('Calibri', 15),
        )
        self.area_label.grid(row=1, column=2, padx=10, pady=(10, 0), sticky='ew', )

        print('\t• Filter labels - ✓')

        print()

        # filter entries
        self.name_filter = ctk.CTkEntry(
            master=self.filters_panel,
            font=('Calibri', 15),
            width=200,
        )
        self.name_filter.grid(row=2, column=0, padx=10, pady=(0, 10),)
        print('\t• Name filter - ✓')

        self.location_filter = ctk.CTkOptionMenu(
            master=self.filters_panel,
            font=('Calibri', 15),
            values=['Not selected', '1', '2', '3'],
            variable=self.location_filter_var,
            fg_color='darkgray',
            text_color='black',
            button_color='darkgray',
            button_hover_color='gray',
            width=200,
        )
        self.location_filter.grid(row=2, column=1, padx=10, pady=(0, 10),)
        print('\t• Location filter - ✓')

        self.area_filter = ctk.CTkSlider(
            master=self.filters_panel,
            variable=self.area_filter_var,
            from_=0,
            to=100,
            command=self.update_area_filter_label,
            progress_color=('gray', 'darkgray'),
            button_color=('gray', 'darkgray'),
            button_hover_color=('gray', 'darkgray'),
            width=200,
        )
        self.area_filter.grid(row=2, column=2, padx=10, pady=(0, 10),)

        self.state_filter = ctk.CTkOptionMenu(
            master=self.filters_panel,
            font=('Calibri', 15),
            values=['Not selected', 'Excellent', 'Good', 'Medium'],
            variable=self.state_filter_var,
            fg_color='darkgray',
            text_color='black',
            button_color='darkgray',
            button_hover_color='gray',
            width=200,
        )
        self.state_filter.grid(row=2, column=3, padx=10, pady=(0, 10),)
        print('\t• State filter - ✓')

        self.price_filter = ctk.CTkOptionMenu(
            master=self.filters_panel,
            font=('Calibri', 15),
            values=['Not selected', '1', '2', '3'],
            variable=self.price_filter_var,
            fg_color='darkgray',
            text_color='black',
            button_color='darkgray',
            button_hover_color='gray',
            width=200,
        )
        self.price_filter.grid(row=2, column=4, padx=10, pady=(0, 10),)
        print('\t• Price filter - ✓')

        self.apply_filters_button = ctk.CTkButton(
            master=self.filters_panel,
            font=('Calibri', 15),
            text='Apply filters',
            fg_color='darkgray',
            hover_color='gray',
            text_color='black',
            command=self.apply_filters,
        )
        self.apply_filters_button.grid(row=3, column=0, padx=400, pady=(20, 10), sticky='ew', columnspan=5,)
        print()
        print('\t• Apply filters button - ✓')

        print()
        print('-' * 50)

    def update_area_filter_label(self, value):
        self.area_label.configure(text=f'Area: {int(float(value))}')

    # menu commands
    def initialize_menu(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.hosts_options = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Hosts functions', menu=self.hosts_options)
        self.hosts_options.add_command(label='Add studliving', command= self.hosts_add)

        self.scripts_options = tk.Menu(self.menu)
        self.menu.add_cascade(label='Scripts', menu=self.scripts_options)
        self.scripts_options.add_command(label='Format csv files', command=self.format_csv)
        self.scripts_options.add_command(label='Import studlivings', command=self.import_studlivings)

        print('\t• Menu - ✓')

    def hosts_add(self):
        try:
            if self.hosts_add is None or not self.hosts_add.winfo_exists():
                from hosts_add import HostsApp
                self.hosts_add = HostsApp(self)

                # Set a protocol to track when the window is closed
                self.hosts_add.protocol("WM_DELETE_WINDOW", self.on_hosts_add_close)
            else:
                self.hosts_add.focus()
        except (AttributeError, tk.TclError):
            from hosts_add import HostsApp
            self.hosts_add = HostsApp(self)
            self.hosts_add.protocol("WM_DELETE_WINDOW", self.on_hosts_add_close)

        print('# Adding studliving debug message')
        print('-' * 50)

    def on_hosts_add_close(self):
        if self.hosts_add is not None:
            self.hosts_add.destroy()
            self.hosts_add = None
            self.refresh_ui()

    def refresh_ui(self):
        self.colivings_df = pd.read_csv(self.COLIVINGS_PATH)

        self.destroy_all_labels()

        if not self.colivings_df.empty:
            self.load_csv_data()

        self.check_csv_contents()

    def format_csv(self):
        for frame in self.form_frames:
            frame.destroy()
        self.form_frames.clear()

        self.colivings_df = pd.DataFrame(columns=self.colivings_df.columns)
        self.colivings_df.to_csv(self.COLIVINGS_PATH, index=False)

        self.check_csv_contents()

    def import_studlivings(self):
        Script().import_samples(self.COLIVINGS_PATH)
        self.refresh_ui()

    def apply_filters(self):
        # filtering logic

        print()
        print("# Apply filters button's used")
        print()
        print('-' * 50)

    # options list initialization
    def initialize_options_list(self):
        self.options_frame = ctk.CTkFrame(
            master=self,
        )
        self.options_frame.pack(fill='both', expand=True, pady=(5, 0),)

    def empty_label_initialization(self):
        if self.colivings_df.empty:
            self.empty_label = ctk.CTkLabel(
                master=self.options_frame,
                text='Database is currently empty',
                font=('Calibri', 20),
            )
            self.empty_label.pack(fill=tk.BOTH, expand=True)
        else:
            if getattr(self, 'empty_label', None) and self.empty_label.winfo_exists():
                self.empty_label.destroy()

        print()
        print('# Options initialization debug message')
        print('\t• Options list - ✓')
        print()
        print('-' * 50)

    def check_csv_contents(self):
        self.colivings_df = pd.read_csv(self.COLIVINGS_PATH)

        if self.colivings_df.empty:
            self.destroy_all_labels()

            if not getattr(self, 'empty_label', None):
                self.empty_label = ctk.CTkLabel(master=self.options_frame,
                                                text='Database is currently empty',
                                                font=('Calibri', 20))
                self.empty_label.pack(fill=tk.BOTH, expand=True)
                return False
        else:
            if getattr(self, 'empty_label', None):
                self.empty_label.destroy()
                self.empty_label = None

                return True

        self.after(3000, self.check_csv_contents)

    def destroy_all_labels(self):
        for i in self.form_frames:
            i.destroy()

    def load_csv_data(self):
        names = self.colivings_df['Name'].to_list()
        locations = self.colivings_df['Location'].to_list()
        areas = self.colivings_df['Area'].to_list()
        states = self.colivings_df['State'].to_list()
        prices = self.colivings_df['Price'].to_list()

        for i in range(len(self.colivings_df)):
            self.form_initialization(names[i], locations[i], areas[i], states[i], prices[i])

    def form_initialization(self, name, location, area, state, price):
        print([name, location, area, state, price])
        form_frame = ctk.CTkFrame(
            master=self.options_frame,
            height=50,
        )
        form_frame.pack(anchor='n', fill=tk.X, pady=(10, 0), padx=10)
        self.form_frames.append(form_frame)

        labels = [f'${price}/month', state, f'{area} m²', location]

        name_label = ctk.CTkLabel(
            master=form_frame,
            text=name,
            font=('Calibri', 20),
        )
        name_label.pack(side=tk.LEFT, padx=10, pady=10,)

        for label in labels:
            if label != state:
                form_label = ctk.CTkLabel(
                    master=form_frame,
                    text=label,
                    font=('Calibri', 20),
                )
                form_label.pack(side=tk.RIGHT, padx=10, pady=10,)
            else:
                colors = {'Excellent': 'lightgreen', 'Good': 'yellow', 'Medium': 'orange'}
                form_label = ctk.CTkLabel(
                    master=form_frame,
                    text=state,
                    text_color=colors[state],
                    font=('Calibri', 20),
                )
                form_label.pack(side=tk.RIGHT, padx=10, pady=10,)

    # main functionality
    def save_data_to_filters_panel(self):
        pass


if __name__ == '__main__':
    main_app = MainApp()

