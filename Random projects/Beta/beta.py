import os
import pandas as pd
from sources.authentication import LoginWindow


def create_files():
    if not os.path.exists('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/data.csv'):
        df = pd.DataFrame({
            'Login': [],
            'Password': []
        })
        df.to_csv('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/data.csv', index=False)

    if not os.path.exists('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/colivings.csv'):
        df = pd.DataFrame({
            'Login': [],
            'Password': []
        })
        df.to_csv('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/colivings.csv', index=False)


if __name__ == '__main__':
    create_files()
    if LoginWindow():
        print('Login successful!')
