'''
Takes tabular data and melts it such into a "flat" structure. 

of timeseries (columnwise dt, value with the code in the first row and the second column for each series 
'''
import csv
import sys
import StringIO

def flatten(data, id_col_indx, num_cols):
    '''
    data - rows of entries, with headings assumed to be in the first row
    id_col_indx - these are the rows that are going to be repeated for each value in the value_cols
    num_cols - this the the number of columns per series of data (usually 2)
    
    returns a list of data of lists
    '''
    rt = []
    codes = data[0]
    for row in data[1:]:
      
        ncols = len(row)
        if ncols % num_cols:
            msg = "This row %s has %s columns which is not a multiple of %s" %(row,ncols,num_cols)
            raise ValueError(msg)
        
        for cur_indx in range(0, ncols, num_cols):
            
            id = codes[cur_indx + id_col_indx]
            
            item = row[cur_indx:cur_indx + num_cols]
            has_data = bool(item[0])
            
            if not has_data:
                continue
            
            new_row = [id]
            new_row.extend(item)
            rt.append(new_row)
        
    return rt 
    
    

def flatten_file(fname, id_col_indx, num_cols):
    '''
    handles the file version of flatten as opposed to data
    returns the data formatted as a csv file
    this is useful for when using it as part of a script
    as an additional feature it adds headings if they exist
    '''
    reader = csv.reader(open(fname))
    data = list(reader)
    reader = None
    
    result = flatten(data, id_col_indx, num_cols)
    return result
    

def tocsv(data, headings = None):
    out = StringIO.StringIO()
    writer = csv.writer(out, lineterminator = '\n')
    if headings:
        writer.writerow(headings)
    writer.writerows(data)
    writer = None
    out_result = out.getvalue()
    return out_result    


def print_usage():
    print '''
           This usage is incorrect
           Fix it
           '''.strip()
    

if __name__ == '__main__':
    
    
    nargs = len(sys.argv)
    if nargs < 2:
        print_usage()
        sys.exit(1)
    
    fname = sys.argv[1]
    
    if nargs > 2:
        id_col_indx = int(sys.argv[2])
    else:
        id_col_indx = 0
    
    if nargs > 3:
        cols_per_series = int(sys.argv[3])
    else:
        cols_per_series = 1
    
    result = flatten_file(fname, id_col_indx, cols_per_series)
    
    fmt_result = tocsv(result)
    sys.stdout.write(fmt_result) 
        
     