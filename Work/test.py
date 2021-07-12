import csv

with open('Data/prices.csv', 'r') as f:
    csv_reader=csv.reader(f)
    for line in csv_reader:
        print(line)

