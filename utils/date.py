#===============================
import datetime
import time
def convert_uk_dt(sdt):
    def uk_dt(sdt):
        d , mo , yr = sdt.split(' ')[0].split('/')
        return (d, mo, yr)
    dt = _convert_dt(sdt, uk_dt)
    return dt

def convert_us_dt(sdt):
    def us_dt(sdt):
        mo , d , yr = sdt.split(' ')[0].split('/')
        return (d, mo, yr)
    dt = _convert_dt(sdt, us_dt)
    return dt

def _convert_dt(sdt, fn):
    try:
        d , mo , yr = fn(sdt)
    except ValueError ,e:
        raise ValueError("Date %s not correct format" %sdt)
    d = int(d)
    mo = int(mo)
    
    if len(yr) <> 4:
        yr = int(yr)
        if yr < 60:
            yr += 2000
        elif yr < 99:
            yr +=  1900
        else:
            raise TypeError,"A 4 digit year is required"
    yr = int(yr)
    try:
        rt = datetime.datetime(yr,mo,d)
    except Exception, e:
        raise ValueError("Err: %s for dt %s" %(e,sdt))
    
    return rt 

dateconverters = {'US' : convert_us_dt,
                  'UK' : convert_uk_dt,
                  }

def fromYYYYMMDD(yyyymmdd):
    dt = str(yyyymmdd)
    yr = int(dt[:4])
    mo = int(dt[4:6])
    dy = int(dt[6:])
    
    rt = datetime.date(yr, mo, dy)
    return rt

toYYYYMMDD  = lambda dt : dt.strftime('%Y%m%d')    

date2timestamp = lambda dte : int(time.mktime(dte.timetuple()))

timestamp2date = lambda ts : datetime.datetime.fromtimestamp(ts)

def get_dt_convert_fn(dt_fmt):
    global dateconverters
    fn = dateconverters.get(dt_fmt, None)
    if fn is None:
        raise ValueError("There is no date converter function for fmt %s" %dt_fmt)
    return fn

def get_dt_str_fmt(dt_fmt):
    dt_str_fmts = {'US' : '%m/%d/%Y',
                   'UK' : '%d/%m/%Y'
                   }
    
    rt = dt_str_fmts.get(dt_fmt, None)
    if rt is None:
        raise ValueError("There is no date string format for fmt %s" %dt_fmt)
    return rt

def to_date(dt):
    """ 
    takes either a date or datetime instance and returns a date
    this is to assist with date comparisons which can't compare 
    a date and datetime instance
    """
    if hasattr(dt, 'date'):
        dt = dt.date()
    return dt

def to_datetime(dt):
    """ 
    takes either a date or datetime instance and returns a date
    this is to assist with date comparisons which can't compare 
    a date and datetime instance
    """
    if not hasattr(dt, 'date'):
        try:
            d = dt.day
        except Exception, e:
            pass
        mo = dt.month
        yr = dt.year
        rt = datetime.datetime(yr, mo, d)
    else:
        rt = dt
    return rt

#===============================

def eom_dt(dt, number_months):
    month = dt.month
    yr = dt.year
    if number_months == 0:
        new_month = month + 1
        if new_month ==13:
            new_month = 1
            yr += 1
    elif number_months < 0:
        new_month = month
        number_months += 1 
    
    elif number_months > 0:
        new_month = month + 2
        if new_month >12:
            yr += new_month // 12
            new_month = new_month % 12
        number_months -= 1
    else:
        raise ValueError("This should never happen")
    
    dt = datetime.date(yr, new_month, 1)
    dt -= datetime.timedelta(days = 1)
    if number_months:
        return eom_dt(dt, number_months)
    else:
        return dt
        