# pcost.py
import csv

def portfolio_cost(filename):

    total_cost=0.0

    with open (filename,'rt') as csv_file:
        rows=csv.reader(csv_file)
        headers=next(rows) 
        for rowno, row in enumerate(rows, start=1):
            record=dict(zip(headers, row))
            try:
                no_shares=int(record['shares'])
                price=float(record['price'])
                total_cost+=no_shares*price
            except ValueError:
                print(f'Row {rowno}: Missing data: {row}')
    return total_cost 

# I know leaving 'dead' code in is messy, but this is so I remeber how to read in data from a file so I don't forget!
# if len(sys.argv)==2:
#     filename=sys.argv[1]
# else:
#     filename=input('Enter a filename:')

cost = portfolio_cost('c:/Users/znc46146/Documents/practical-python/Work/Data/portfoliodate.csv')
print('Total cost:', cost)