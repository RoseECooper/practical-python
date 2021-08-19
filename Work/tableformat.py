'''
Seperate class to format the table of data returned by report.py.
Enables a variety of different output types. 
'''

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError() 

class TextTableFormatter(TableFormatter):
    '''
    Output portfolio data in a plain text format.
    '''
    def headings (self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10+' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in a CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in a html format.
    '''
    def headings (self, headers):
        print('<tr>', end='') 
        for h in headers: 
            print(f'<th>{h}</th>', end='')
        print('</tr>')
        print()

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata: 
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(name):

    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

def print_table(objects, columns, formatter):
    '''
    Make a formatted table witht he desired columns
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)