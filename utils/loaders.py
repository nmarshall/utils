from parser import load_csv_dict

class csvLoader(object):
    '''
    Used for taking csv files and converting them into a format that an underlying
    object can use.
    '''
    
    Loader = None
    
    cleaners = {}
    
    def __init__(self, path, heading_mappings, dt_fmt = 'UK', loader = None, heading_indx_row = 0):
        self._loader = loader or self.Loader()
        
        data = load_csv_dict(path, dt_fmt, heading_indx_row)
        translated_data = self._translate_data(data, heading_mappings)
        self._clean_data(translated_data)
        
        self._data = translated_data
        self._result = None
    
    def _clean_data(self, data):
        '''
        responsible for changing variable values as required
        it uses a dictionary of form { variable_name : clean_function ..}
        '''
        cleaners = self.cleaners
        for attr, fn in cleaners.items():
            for row in data:
                val = row[attr]
                clean_val = fn(val)
                row[attr] = clean_val                
    
    def _translate_data(self, data, mappings):
        '''
        changes the heading names used in the underlying file
        to the variable names that will be used in the underlying class
        '''
        rt = []
        for row in data:
            tmp = {}
            for cur_heading, new_heading in mappings.items():
                val = row[cur_heading] ## Could raise a nice error here
                if isinstance(new_heading, list):
                    for h in new_heading:
                        tmp[h] = val
                else:
                    tmp[new_heading] = val
            rt.append(tmp)
        return rt 
    
    def load(self):
        loader = self._loader
        if loader is None:
            msg = "There is no loader associated with this class"
            raise ValueError(msg)
            
        result = self._result
        if result is None:
            data = self._data
            result = loader.load(data)
        return result
        