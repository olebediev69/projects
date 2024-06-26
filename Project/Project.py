from colorama import Fore, Style
from time import sleep
import csv

fieldnames = ['Path','Metrics']

new_append = {'Path':'/Users/oleksandrlebediev/PycharmProjects/projects/Project/incomeStatement-AAPL-annual.csv','Metrics':[12,13,14]}

def add_path(fieldnames,append):

    with open('metrics.csv','r',newline='') as csvread:
        rows = []
        reader = csv.DictReader(csvread)
        for row in reader:
            rows.append(row)
        rows.append(append)

    with open('metrics.csv','w',newline='') as csvappend:
        appender = csv.DictWriter(csvappend, fieldnames = fieldnames)
        appender.writeheader()
        for row in rows:
            appender.writerow(row)


# main logic block
