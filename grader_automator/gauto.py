import csv

file_to_read = input('Enter filepath: e.g. blah.csv: ')
# print(type(file_to_read))

with open(file_to_read) as csvfile:
    linereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(linereader)
    header[0] = ''

    cols = len(header)

    with open('auto_output.txt', 'w') as outfile:

        for row in linereader:
            headers_included =  [': '.join([colname, row[i]]) for i, colname in enumerate(header)]
            headers_included[0] = headers_included[0].strip(': ') # just the name line removed

            # pesky leading space removed for all lines
            # headers_included = list(map(str.strip, headers_included)) 
            
            headers_included.append('\n')
            outfile.write('\n'.join(headers_included))
            # print('\n'.join(headers_included))
