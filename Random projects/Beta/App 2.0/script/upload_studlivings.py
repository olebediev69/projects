import pandas as pd
import os


class Script:
    def __init__(self):
        self.path = '/Users/oleksandrlebediev/PycharmProjects/projects/Random projects/Beta/App 2.0/script/sample.csv'
        self.studlivings = pd.DataFrame([
            {
                'Name': "Strays but not kids",
                'Location': "boul. Lesi Ukrainky 30B",
                'Area': 550,
                'State': 'Medium',
                'Price': 5500
            },
            {
                'Name': 'Your fever dream',
                'Location': 'st. Proviantska 3',
                'Area': 200,
                'State': 'Good',
                'Price': 3215
            },
            {
                'Name': 'Girls and insanity',
                'Location': 'st. Levandovska 5',
                'Area': 315,
                'State': 'Excellent',
                'Price': 3900
            }
        ])

    def create_sample(self):
        if not os.path.exists(self.path):
            df = pd.DataFrame({
                'Name': [],
                'Location': [],
                'Area': [],
                'State': [],
                'Price': [],
            })
            df.to_csv(self.path, index=False)

    def import_samples(self, path):
        self.create_sample()
        self.studlivings.to_csv(path, index=False)


if __name__ == '__main__':
    Script()
