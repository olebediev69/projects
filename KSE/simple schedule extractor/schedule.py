import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from os import path
from colorama import Fore, Style, Back
import pandas as pd
import warnings
import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


class schedule(tk.Tk):
    def __init__(self):
        super().__init__()

        # variables initialization
        self.browse_final_path_button = None
        self.browse_final_path = None
        self.analyse_and_extract_button = None
        self.analyse_and_extract = None
        self.final_path_label = None
        self.analyse_and_save_frame = None
        self.clear_subjects_button = None
        self.subjects_frame = None
        self.add_subjects_button = None
        self.subjects_label = None
        self.subjects_entry = None
        self.clear_excel_path_button = None
        self.browse_excel_path_label = None
        self.browse_excel_path_button = None
        self.file_selection_frame = None
        self.primary_file_path = None
        self.final_path = None
        self.schedule_df = None
        self.subjects_list = []

        # window parameters
        self.title("Schedule Extractor")
        self.geometry("400x300")
        self.resizable(False, False)

        # widgets initialization
        self.initialize_file_selection_section()
        self.initialise_subjects_entry_section()
        self.analyze_and_save_section()

        self.test_section()

        self.mainloop()

    # gui initialization functions
    def initialize_file_selection_section(self):
        self.file_selection_frame = ctk.CTkFrame(master=self)
        self.file_selection_frame.rowconfigure((0, 1), weight=1)
        self.file_selection_frame.columnconfigure((0, 1), weight=1)
        self.file_selection_frame.pack(fill=tk.X)

        self.browse_excel_path_label = ctk.CTkLabel(
            master=self.file_selection_frame,
            text="No file selected",
            font=('Arial', 12)
        )
        self.browse_excel_path_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.browse_excel_path_button = ctk.CTkButton(
            master=self.file_selection_frame,
            text='Select file',
            font=('Arial', 12),
            command=self.select_excel_path
        )
        self.browse_excel_path_button.grid(row=1, column=0, padx=(10, 5), pady=10, sticky='ew')

        self.clear_excel_path_button = ctk.CTkButton(
            master=self.file_selection_frame,
            text='Clear file',
            font=('Arial', 12),
            command=self.clear_excel_path
        )
        self.clear_excel_path_button.grid(row=1, column=1, padx=(5, 10), pady=10, sticky='ew')

    def select_excel_path(self):
        filepath = filedialog.askopenfilename(title='Select a file')
        if filepath and filepath.endswith('.xlsx'):
            self.browse_excel_path_label.configure(text=f'Selected file: {path.basename(filepath)}')
            self.primary_file_path = filepath
        else:
            messagebox.showerror(title='Error', message='Please select an excel file.')
        print(f'\n💾 Path was successfully selected: {self.primary_file_path} {Fore.YELLOW}*{Style.RESET_ALL}')

    def clear_excel_path(self):
        self.browse_excel_path_label.configure(text='No file selected')
        self.primary_file_path = None
        print(f'\n🗑️ Path was successfully cleared')

    def initialise_subjects_entry_section(self):
        self.subjects_frame = ctk.CTkFrame(master=self)
        self.subjects_frame.rowconfigure((0, 1, 2), weight=1)
        self.subjects_frame.columnconfigure((0, 1), weight=1)
        self.subjects_frame.pack(fill=tk.X, pady=2)

        self.subjects_label = ctk.CTkLabel(
            master=self.subjects_frame,
            text='No subjects selected',
            font=('Arial', 10)
        )
        self.subjects_label.grid(row=0, padx=10, pady=(0, 10), sticky='we', columnspan=2)

        self.subjects_entry = ctk.CTkEntry(master=self.subjects_frame)
        self.subjects_entry.grid(row=1, padx=10, pady=(0, 10), sticky='we', columnspan=2)

        self.add_subjects_button = ctk.CTkButton(
            master=self.subjects_frame,
            text='Add subjects',
            font=('Arial', 12),
            command=self.add_subject_button
        )
        self.add_subjects_button.grid(row=2, column=0, padx=(10, 5), pady=(0, 10), sticky='we')

        self.clear_subjects_button = ctk.CTkButton(
            master=self.subjects_frame,
            text='Clear subjects',
            font=('Arial', 12),
            command=self.clear_subjects
        )
        self.clear_subjects_button.grid(row=2, column=1, padx=(10, 5), pady=(0, 10), sticky='we')

    def add_subject_button(self):
        if self.primary_file_path:
            if self.subjects_entry.get() and self.subjects_entry.get() not in self.subjects_list:
                self.subjects_list.append(self.subjects_entry.get())
                self.subjects_label.configure(text=f'{", ".join(self.subjects_list)}')
                print(f'\n📘 Subject selected: {self.subjects_entry.get()}')
                self.subjects_entry.delete(0, 'end')
            else:
                messagebox.showerror(title='Error', message='Subject already exists or the field is empty.')
        else:
            messagebox.showerror(title='Error', message='Please select a file first.')

    def clear_subjects(self):
        if self.subjects_list:
            self.subjects_list.clear()
            self.subjects_entry.delete(0, 'end')
            self.subjects_label.configure(text='')
            print(f"\n🗑️ Subjects' list cleared")
        else:
            messagebox.showerror(title='Error', message="Please enter the subject name first.")

    def analyze_and_save_section(self):
        self.analyse_and_save_frame = ctk.CTkFrame(master=self)
        self.analyse_and_save_frame.rowconfigure((0, 1), weight=1)
        self.analyse_and_save_frame.columnconfigure((0, 1), weight=1)
        self.analyse_and_save_frame.pack(fill=tk.BOTH, expand=True)

        self.final_path_label = ctk.CTkLabel(
            master=self.analyse_and_save_frame,
            text='No final path chosen',
            font=('Arial', 12)
        )
        self.final_path_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        
        self.browse_final_path_button = ctk.CTkButton(
            master=self.analyse_and_save_frame,
            text='Browse files',
            font=('Arial', 12),
            command=self.select_final_path
        )
        self.browse_final_path_button.grid(row=1, column=0, padx=(10, 5), pady=10, sticky='we')
        
        self.analyse_and_extract_button = ctk.CTkButton(
            master=self.analyse_and_save_frame,
            text='Analyse & extract',
            font=('Arial', 12),
            command=self.analyse_extract
        )
        self.analyse_and_extract_button.grid(row=1, column=1, padx=(5, 10), pady=10, sticky='we')

    def select_final_path(self):
        folder_path = filedialog.askdirectory(title='Select Folder to Save Analysis')
        if folder_path:
            self.final_path_label.configure(text=f'Selected file: {folder_path}')
            self.final_path = folder_path
            print(f"\n📂 Selected folder: {folder_path}")
            return folder_path
        else:
            messagebox.showerror(title='Error', message='Please select a final destination for the analysis file.')

    # excel analysis functions
    def fix_headers_excel(self):
        schedule_df = pd.read_excel(self.primary_file_path, engine='openpyxl', header=None)
        for index, week in enumerate(schedule_df.iloc[:, 0]):
            if "тижд." in str(week) and index == 0:
                corrected_headings = pd.Series(schedule_df.iloc[index])
                corrected_headings = corrected_headings.ffill()
                schedule_df.iloc[index] = corrected_headings
            elif "тижд." in str(week) and index != 0:
                refined_headings = pd.Series(schedule_df.iloc[index])
                refined_headings = refined_headings.ffill()
                schedule_df.iloc[index] = refined_headings

        print(f'\n⚙️ An excel file has been analyzed successfully.')
        return schedule_df

    def create_personal_schedule(self):
        # weeks[-1] - week
        # excel_file.iloc[0, i] - day
        # excel_file.iloc[i, 0] - time
        # element - subject
        if self.final_path:
            excel_file = self.fix_headers_excel()

            weeks = ['1 тижд.']
            time_slots = ['08:30:00', '10:00:00', '11:30:00', '13:30:00', '15:00:00', '16:30:00', '18:00:00', '19:30:00']
            days = ['ПОНЕДІЛОК', 'ВІВТОРОК', 'СЕРЕДА', 'ЧЕТВЕР', "П'ЯТНИЦЯ"]
            subjects = {}

            for i in range(1, excel_file.shape[1]):
                for element in excel_file.iloc[i]:
                    if 'тижд.' in str(element):
                        weeks.append(element)
                    if (element is not np.nan) and element in self.subjects_list:
                        current_week = weeks[-1]
                        day = excel_file.iloc[0, i]
                        time = excel_file.iloc[i, 0]
                        subject = element

                        subjects[(current_week, day, time)] = subject

            all_weeks = []
            for week in weeks:
                schedule = pd.DataFrame(index=time_slots, columns=['Тиждень'] + days)
                schedule['Тиждень'] = week

                for (week_key, day, time), subject in subjects.items():
                    if week_key == week:
                        schedule.loc[time, day] = subject

                all_weeks.append(schedule)
                all_weeks.append(pd.DataFrame([[''] * (len(days) + 1)], columns=['Тиждень'] + days))

            final_schedule = pd.concat(all_weeks, ignore_index=False)

            final_schedule.to_excel((self.final_path + "/schedule.xlsx"), index_label="Time Slot")
            print(f'\n✅ The schedule has been extracted to: {self.final_path + '/schedule.xlsx'}')
            exit()
        else:
            messagebox.showerror(title='Error', message='Please select a final destination for the schedule.')

    def analyse_extract(self):
        self.create_personal_schedule()

    # test section (you can delete two functions below)
    def test_section(self):
        self.test_button = ctk.CTkButton(
            master=self,
            text='Test',
            font=('Arial', 12),
            command=self.test_function
        )
        self.test_button.pack(padx=10, pady=10)

    def test_function(self):
        pass


if __name__ == '__main__':
    schedule = schedule()
