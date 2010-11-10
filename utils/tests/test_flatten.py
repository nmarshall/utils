from unittest import TestCase
import os
import flatten

__all__ = ['TestFlattenUnitTest',
           ]

class TestFlattenUnitTest(TestCase):
    
    def test_flatten_file(self):
        pdir = os.path.dirname(__file__)
        src_fname = os.path.join(pdir, '..', 'fixtures', 'flatten_test.csv')
        number_cols_per_item = 2
        id_col_indx = 1 
        
        result = flatten.flatten_file(src_fname, id_col_indx, number_cols_per_item)
        
        nrows = len(result)
        self.assertEqual(nrows,12)
        
        last_value = result[-1][-1]
        self.assertEqual(last_value,'LAST')
    
#    def test_flatten_file(self):
#        pdir = os.path.dirname(__file__)
#        src_fname = os.path.join(pdir, '..', 'fixtures', 'ratesraw.csv')
#        number_cols_per_item = 2
#        id_col_indx = 1 
#        
#        result = flatten.flatten_file(src_fname, id_col_indx, number_cols_per_item)
#        last_row = result[-1]
#        last_value = result[-1][-1]
#        self.assertEqual(last_value,'LAST')
        