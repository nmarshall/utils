from djutils import slugify
import csv

class StringParser(object):
    
    def __init__(self):
        self._fns = []
    
    def add(self, fn):
        self._fns.append(fn)
    
    def parse(self, str):
        fns = self._fns
        for fn in fns:
            try:
                val = fn(str)
            except Exception, e:
                val = None
            if not val is None:
                return val
        result = str.strip()
        return result

from misc import to_float
from date import get_dt_convert_fn

def to_numeric(str):
    if '.' in str:
        val = to_float(str)
    elif '-' in str and len(str.strip())==1:
        val = 0.0
    else:
        val = int(str)
    return val



def create_string_parser(dt_fmt):
    dt_fn = get_dt_convert_fn(dt_fmt)
    #dt_fn = lambda strdt : fn(strdt).date()
    parser = StringParser()
    parser.add(dt_fn)
    parser.add(to_numeric)
    return parser
    

def load_csv_dict(path, dt_fmt = 'UK', heading_row=0):
    parser = create_string_parser(dt_fmt)
    rt = []
    f = open(path)
    for r in range(heading_row):
        f.readline()
    reader = csv.DictReader(f)
    for row in reader:
        tmp = {}
        for k , v in row.items():
            if not k=='':
                tmp[k] = parser.parse(v)
        rt.append(tmp)
    f.close()
    return rt 




    