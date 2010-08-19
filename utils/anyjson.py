try:
    import json
except:
    import simplejson as json

from date import date2timestamp    
import datetime    
class JSONRPCEncoder(json.JSONEncoder):
    """
    Provide custom serializers for JSON-RPC.
    """
    def default(self, obj):
        if isinstance(obj, datetime.date) or isinstance(obj, datetime.datetime):
            return date2timestamp(obj)
        else:
            raise exceptions.JSONEncodeException("%r is not JSON serializable" % (obj,))
        

class jsonPickler(object):
    
    def dumps(self, obj, **kwargs):
        return json.dumps(obj, cls=JSONRPCEncoder, **kwargs)
    
    def loads(self,sobj):
        return json.loads(sobj)
