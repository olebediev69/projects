import pandas as pd
from tabulate import tabulate


class Todo:
    def __init__(self):
        self.menu = '\nChoose an option:\n(a) show the current tasks\n(b) add a new task\n(c) Exit\n'
        self.df = pd.read_csv('todo.csv')

    def show_database(self):
        if self.df.empty:
            print('\nThe database is empty')
        else:
            print(tabulate(self.df, headers='keys', tablefmt='fancy_grid'))

    def show_menu(self):
        print(self.menu)
        choice = input('Enter your choice: ')
        if choice == 'a':
            self.show_database()
        elif choice == 'b':
            self.add_task()
        elif choice == 'c':
            exit('\nExiting...')

    def add_task(self):
        task, status = input('Format (task-status): ').split('-')
        adding_df = pd.DataFrame([{'Task': task, 'Status': status}])
        self.df = pd.concat([self.df, adding_df], ignore_index=True)
        self.df.to_csv('todo.csv', index=False)


# Create a single instance of Todo
todo = Todo()

while True:
    todo.show_menu()
