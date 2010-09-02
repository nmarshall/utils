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
    from django import forms
    import json
    
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
    
    class JSONWidget(forms.Textarea):
        def render(self, name, value, attrs=None):
            if not isinstance(value, basestring):
                value = json.dumps(value, indent=2)
            return super(JSONWidget, self).render(name, value, attrs)
 
    class JSONFormField(forms.CharField):
        def __init__(self, *args, **kwargs):
            kwargs['widget'] = JSONWidget
            super(JSONFormField, self).__init__(*args, **kwargs)
 
        def clean(self, value):
            if not value: return
            try:
                return json.loads(value)
            except Exception, exc:
                raise forms.ValidationError(u'JSON decode error: %s' % (unicode(exc),))
 
    class JSONField(models.TextField):
        __metaclass__ = models.SubfieldBase
 
        def formfield(self, **kwargs):
            return super(JSONField, self).formfield(form_class=JSONFormField, **kwargs)
 
        def to_python(self, value):
            if isinstance(value, basestring) and value:
                value = json.loads(value)
            return value
 
        def get_db_prep_save(self, value):
            if value is None: return
            return json.dumps(value)
 
        def value_to_string(self, obj):
            value = self._get_val_from_obj(obj)
            return self.get_db_prep_value(value)
    
except Exception, e:
    print e
    
def slugify(value, rtx = '-'):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicode(re.sub('[^\w\s-]', '', value).strip())
    return mark_safe(re.sub('[-\s]+', rtx, value))