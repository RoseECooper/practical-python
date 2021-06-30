# Exercises from practical-python course.
# Currently completed exercise 2.7, which is the final part of section 2.2 containers.

import csv

def read_portfolio(filename):

    '''
    Function to read in the information from the portfolio file 
    into a dictionary.
    '''

    portfolio=[]

    with open (filename) as csv_file: 
        rows=csv.reader(csv_file)
        headers=next(rows) 
        for row in rows:
            record=dict(zip(headers,row))
            stock={
                'name':record['name'],
                'shares':int(record['shares']),
                'price':float(record['price'])
            }
            portfolio.append(stock)
    return portfolio 

def read_prices(filename):

    '''
    Function to read in the information from the prices file
    '''

    prices={}

    with open(filename) as csv_file:
        rows=csv.reader(csv_file)
        for row in rows:
            try:
                prices[row[0]]=float(row[1])
            except IndexError:
                pass
    return prices

def stock_value_change(portfolio, prices):

    '''
    Function to take the information from portfolio and prices and calculate the 
    difference in the value of the stocks. 
    '''

    rows=[]

    for stock in portfolio:
        current_price=prices[stock['name']]
        difference=current_price-stock['price']
        summary=(stock['name'], stock['shares'], current_price, difference)
        rows.append(summary)
    return rows

# Read in files
portfolio=read_portfolio('c:/Users/znc46146/Documents/practical-python/Work/Data/portfolio.csv')
prices=read_prices('c:/Users/znc46146/Documents/practical-python/Work/Data/prices.csv')

# Generate output of stock_value_change and construct a structured print statement to view the data.
report=stock_value_change(portfolio, prices)

headers=('Name', 'Shares', 'Price', 'Difference')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ')*len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
