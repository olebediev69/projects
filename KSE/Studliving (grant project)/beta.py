import os
import pandas as pd


def create_files():
    if not os.path.exists('/Random projects/Studliving (grant project)/csvs/data.csv'):
        df = pd.DataFrame({
            'Login': [],
            'Password': []
        })
        df.to_csv('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Studliving (grant project)/csvs/data.csv', index=False)

    if not os.path.exists('/Random projects/Studliving (grant project)/csvs/colivings.csv'):
        df = pd.DataFrame({
            'Name': [],
            'Location': [],
            'Area': [],
            'State': [],
            'Price': [],
        })
        df.to_csv('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Studliving (grant project)/csvs/colivings.csv', index=False)


if __name__ == '__main__':
    create_files()

    from sources.authentication import LoginWindow
    from test import AppWindow

    if LoginWindow():
        AppWindow()
