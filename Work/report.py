# Exercises from practical-python course.
# Currently completed exercise 3.1, now on section 3.2

import fileparse

def read_portfolio(filename):
    '''
    Function to read in the information from the portfolio file 
    into a dictionary.
    '''
    with open(filename) as lines:
        return fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])

def read_prices(filename):
    '''
    Function to read in the information from the prices file
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))

def stock_price_change(portfolio, prices):
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

def print_report(table):
    '''
    Function to construct formatted print statement.
    '''
    headers=('Name', 'Shares', 'Price', 'Difference')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ')*len(headers))
    for row in table:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_diff(table):
    '''
    Function to determine if the portfolio has gained or lost value over time.
    '''
    total_diff=0 

    for index, tuple in enumerate(table):
         difference=tuple[3]
         total_diff=total_diff+difference

    print('Total portfolio value change:', total_diff)

    while total_diff>0:
        print('Portfolio gained value')
    else:
        print('Portfolio lost value')

def portfolio_report(portfolio_filename, prices_filename): 
    '''
    Function to read in files and output stocks report in a table along 
    with a statement on how the portfolio has performed
    '''
    portfolio=read_portfolio(portfolio_filename)
    prices=read_prices(prices_filename)

    table=stock_price_change(portfolio, prices)
    print_report(table)
    portfolio_diff(table)

def main(args):
    '''
    Top level function to run report file.
    Can import the file into the console and run the main module. 
    Takes inputs from the command line as input arguments for the files being used. 
    '''
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__=='__main__':
    import sys
    main(sys.argv) 

