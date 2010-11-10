class baseDayCount(object):
    type = 'base'
    
    
    def year_fraction(self, start, until):
        '''
        returns the year fraction
        between two dates        
        '''
        pass
    
    def day_count(self, start, until):
        '''
        returns the number of days between two dates
        '''
        pass
    
    
class DayCount30360(baseDayCount):
    
    def day_count(self, start, until):
        d1, d2 = start.day, until.day
        if d1 == 31:
            d1 -= 1
        if d2 == 31:
            d2 -= 1
        day_diff = (int(d2) - int(d1))  
        mnth_diff = int(until.month) - int(start.month)
        yr_diff = int(until.year) - int(start.year)
        result = day_diff + 30 * mnth_diff + 360 * yr_diff
        return result
        
    def year_fraction(self, start,until):
        day_count = self.day_count(start, until)                      
        result = day_count / 360.0
        return result
        
class DayCountAct360(baseDayCount):
    
    def day_count(self, start, until):
        result = (until - start).days
        return result
        
    def year_fraction(self, start,until):
        day_count = self.day_count(start, until)                      
        result = day_count / 360.0
        return result


def get_day_count(name):
    
    day_counts = {'act/360' : DayCountAct360(),
                  '30/360' : DayCount30360(),
                   }
    
    day_count = day_counts.get(name.lower(), None)
    if day_count is None:
        msg = "No day count with name %s, choices are %s"
        raise ValueError(msg, name, day_counts)
    return day_count