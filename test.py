import pandas as pd
from colorama import Back, Style

data = pd.read_excel('/Users/oleksandrlebediev/Desktop/Розклад для студентів (весняний терм 2025).xlsx', header=None)

def values_substitutor():
    global data
    for index, week in enumerate(data.iloc[:, 0]):
        if "тижд." in str(week) and index == 0:
            refined_headings = pd.Series(data.iloc[index])
            refined_headings = refined_headings.ffill()
            data.iloc[index] = refined_headings
        elif "тижд." in str(week) and index != 0:
            refined_headings = pd.Series(data.iloc[index])
            refined_headings = refined_headings.ffill()
            data.iloc[index] = refined_headings

values_substitutor()
print(data.head(21))