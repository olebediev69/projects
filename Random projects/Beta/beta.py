import os
import pandas as pd
from sources.login import LoginWindow


def create_files():
    if not os.path.exists('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/data.csv'):
        df = pd.DataFrame({
            'Login': [],
            'Password': []
        })
        df.to_csv('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/data.csv', index=False)

    # if not os.path.exists('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/colivings.csv'):
    #     df = pd.DataFrame({
    #         'Login': [],
    #         'Password': []
    #     })
    #     df.to_csv('/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/colivings.csv', index=False)


if __name__ == '__main__':
    login_success = LoginWindow()
    if login_success:
        print('Login successful!')
    else:
        print('Login failed.')