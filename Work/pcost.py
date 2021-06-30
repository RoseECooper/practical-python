# pcost.py
#
# Exercise 1.27

import csv
import sys 

def portfolio_cost(filename):

    total_cost=0.0

    with open (filename,'rt') as csv_file: 
        rows=csv.reader(csv_file)
        headers=next(rows) 
        for row in rows:
            try:
                no_shares=int(row[1])
                price=float(row[2])
                total_cost+=no_shares*price
            except ValueError:
                print('Bad data', row)
    return total_cost 

if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename=input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)