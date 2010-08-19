import ConfigParser
class ListConfigParser(ConfigParser.RawConfigParser):
    def getlist(self , section , option=None):
        if option is None:
            option = section
        result = self.get(section, option)
        assert result[0]  == '['
        assert result[-1] == ']'
        return eval(result)

def to_float(val, sep=','):
    if sep in val:
        tmp = val.split(sep)
        val = ''.join(tmp)
    return float(val)

def to_dict(sample, attrs):
    rt = {}
    for s in sample:
        sattrs = attrs.split('.')
        val = s
        for attr in sattrs:
            val = getattr(val, attr)
        rt[val] = s
    return rt

def dict_to_key(dct):
    itms = list(dct.items())
    itms.sort()
    ky = tuple(itms)
    return ky

