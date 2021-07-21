# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv file into a list of records
    '''

    if select and not has_headers:
        raise RuntimeError('Select requires column headers')

    rows=csv.reader(lines, delimiter=delimiter)

    # set headers (if any)
    headers=next(rows)if has_headers else []

    # If a column selector is given, find the values from the specific columns.
    # Also narrow the set of headers used for resulting dicts. 
    if select: 
        indicies=[headers.index(colname) for colname in select]
        headers=select

    records=[]
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skips rows with no data
            continue
        
        if select: 
            row=[row[index]for index in indicies]

        if types:
            try: 
                row=[func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors: 
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

    # make a dict/tuple depending on headers
        if headers:
            record=dict(zip(headers, row))
        else:
            record=tuple(row)
        records.append(record)
    
    return records 