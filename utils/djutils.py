import re
from django.utils.safestring import mark_safe



def django_choices(vals):
    '''
    vals is an iterable
    '''
    choices = []
    if isinstance(vals,dict):
        for k,v in vals.iteritems():
            choices.append((str(k),str(v)))
    else:
        try:
            for v in vals:
                sv = str(v)
                choices.append((sv,sv))
        except:
            pass
    return choices

try:
    from django.db import models
    class SlugCode(models.CharField):
        
        def __init__(self, rtxchar='_', lower=False, upper = False, **kwargs):
            self.rtxchar = u'%s' % rtxchar
            self.lower   = lower
            self.upper   = upper
            super(SlugCode,self).__init__(**kwargs)
        
        def trim(self, value):
            value = slugify(u'%s'%value, rtx = self.rtxchar)
            if self.lower:
                value = value.lower()
            elif self.upper:
                value = value.upper()
            return value
        
        def pre_save(self, model_instance, add):
            value = getattr(model_instance, self.attname)
            value = self.trim(value)
            setattr(model_instance, self.attname, value)
            return value
except Exception, e:
    print e
    
def slugify(value, rtx = '-'):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicode(re.sub('[^\w\s-]', '', value).strip())
    return mark_safe(re.sub('[-\s]+', rtx, value))