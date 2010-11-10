try:
    import json
except:
    import simplejson as json

from date import date2timestamp
from date import timestamp2date    
import datetime

def date_hook(dct):
    if '__datetime__' in dct:
        return timestamp2date(dct['__datetime__'])
    elif '__date__' in dct:
        return timestamp2date(dct['__date__']).date()
    else:
        return dct
   
class JSONRPCEncoder(json.JSONEncoder):
    """
    Provide custom serializers for JSON-RPC.
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {'__datetime__' : date2timestamp(obj)}
        elif isinstance(obj, datetime.date):
            return {'__date__' : date2timestamp(obj)}
        else:
            raise exceptions.JSONEncodeException("%r is not JSON serializable" % (obj,))
        

class jsonPickler(object):
    
    def dumps(self, obj, **kwargs):
        return json.dumps(obj, cls=JSONRPCEncoder, **kwargs)
    
    def loads(self,sobj, **kwargs):
        if not 'object_hook' in kwargs:
            kwargs['object_hook'] = date_hook
        return json.loads(sobj, **kwargs)
