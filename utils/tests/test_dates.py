from unittest import TestCase
import date
import datetime

__all__ = ['TestDates',
           ]
class TestDates(TestCase):
    
    def test_eomdt(self):
        dt = datetime.date(2009, 12, 29)
         
        dts_period_result = [(dt, 0, datetime.date(2009, 12, 31)),
                             (dt, 1, datetime.date(2010, 1, 31)),
                             (dt, -1, datetime.date(2009, 11, 30)),
                             ]
        
        for val in dts_period_result:
            tdt, period, exp_dt = val
            recv_dt = date.eom_dt(tdt, period)
            
            self.assertEqual(exp_dt, recv_dt)
            