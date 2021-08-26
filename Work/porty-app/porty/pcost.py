# pcost.py
from . import report

def portfolio_cost(filename):
    '''
    Calculate total cost of a stock portfolio
    '''

    portfolio=report.read_portfolio(filename)
    return portfolio.total_cost

# I know leaving 'dead' code in is messy, but this is so I remember how to read in data from a file so I don't forget!
# if len(sys.argv)==2:
#     filename=sys.argv[1]
# else:
#     filename=input('Enter a filename:')

def main(args):
    '''
    Top level function to run pcost file.
    Can import the file into the console and run the main module. 
    Takes inputs from the command line as input arguments for the files being used. 
    '''
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename=args[1]
    print('Total cost: ',portfolio_cost(filename))

if __name__=='__main__':
    import sys
    main(sys.argv)
