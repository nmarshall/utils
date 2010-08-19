from ccy.dates import period
from ccy.tradingcentres import prevbizday
import datetime
class Interval(object):
    
    def __init__(self, edt, dt_or_period):
        if isinstance(dt_or_period, datetime.date) or isinstance(dt_or_period, datetime.datetime):
            sdt = dt_or_period
        else:
            p = period(dt_or_period)
            newdt = edt - datetime.timedelta(days = p.totaldays)
            sdt = prevbizday(newdt, 0)
        
        self._start_dt = sdt
        self._end_dt = edt
    
    def start_date(self):
        return self._start_dt
    
    def end_date(self):
        return self._end_dt

class MTDInterval(Interval):
    
    def __init__(self, edt):
        year = edt.year
        month = edt.month
        
        eom = datetime.date(year, month, 1) - datetime.timedelta(days=1)
        sdt = prevbizday(eom, 0)
        Interval.__init__(self, edt, sdt)
        

def get_interval(period, edt):
    intervals = { 'MTD' : MTDInterval
                 }
    
    if period in intervals:
        klass = intervals[period]
        interval = klass(edt)
    else:
        interval = Interval(edt, period)
    return interval