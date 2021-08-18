# Exercises from practical-python course.
# Currently completed exercise 4.6

import fileparse
from stock import Stock
import tableformat

def read_portfolio(filename):
    '''
    Function to read in the information from the portfolio file 
    into a list of dictionaries.
    '''
    with open(filename) as lines:
        portdicts=fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
    
    portfolio=[Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio

def read_prices(filename):
    '''
    Function to read in the information from the prices file.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))

def make_report_data(portfolio, prices):
    '''
    Function to take the information from portfolio and prices and calculate the 
    difference in the value of the stocks. 
    '''
    rows=[]
    for s in portfolio:
        current_price=prices[s.name]
        change=current_price-s.price
        summary=(s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata, formatter):
    '''
    Function to construct formatted print statement.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata: 
        rowdata=[name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

# def portfolio_diff(reportdata):
#     '''
#     Function to determine if the portfolio has gained or lost value over time.
#     '''
#     total_diff=0 

#     for index, tuple in enumerate(reportdata):
#          change=tuple[3]
#          total_diff=total_diff+change

#     print('Total portfolio value change:', total_diff)

#     while total_diff>0:
#         print('Portfolio gained value')
#     else:
#         print('Portfolio lost value')

def portfolio_report(portfoliofile, pricefile, fmt): 
    '''
    Function to read in files and output stocks report in a table along 
    with a statement on how the portfolio has performed
    '''
    # Read in data files:
    portfolio=read_portfolio(portfoliofile)
    prices=read_prices(pricefile)

    # Create the report data:
    report=make_report_data(portfolio, prices)

    # Print the report in the desired format:
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
#    portfolio_diff(report)

def main(args):
    '''
    Top level function to run report file.
    Can import the file into the console and run the main module. 
    Takes inputs from the command line as input arguments for the files being used. 
    '''
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__=='__main__':
    import sys
    main(sys.argv) 

