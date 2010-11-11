import ConfigParser
class ListConfigParser(ConfigParser.RawConfigParser):
    
    def getlist(self , section , option=None):
        if option is None:
            option = section
        result = self.get(section, option)
        assert result[0]  == '['
        assert result[-1] == ']'
        return eval(result)

class RobustConfigParser(ListConfigParser):
    
    def __init__(self, fname):
        ListConfigParser.__init__(self)
        self.read(fname)
        self._method_fns = self._get_fns()
    
    def _get_fns(self):
        methods = [meth for meth in dir(ListConfigParser) if ('get' in meth and len(meth) > 3)]
        method_fns = [getattr(self, meth) for meth in methods]
        return method_fns
        
    def get_pyobject(self, section, option):
        fns = self._method_fns
        
        for fn in fns:
            try:
                result = fn(section, option)
                return result
            except Exception ,e:
                pass
        
        result = self.get(section, option)
        return result
    
    def todict(self):
        sections = self.sections()
        rt = {}
        for sec in sections:
            sec_opts = {}
            options = self.options(sec)
            for opt in options:
                val = self.get_pyobject(sec, opt)
                sec_opts[opt] = val
            rt[sec] = sec_opts
        return rt