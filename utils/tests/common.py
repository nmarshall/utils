from unittest import TestCase
import os

class CommonTestCase(TestCase):
    
    def fixture_dir(self):
        pdir = os.path.dirname(__file__)
        fdir = os.path.join(pdir, '..', 'fixtures')
        return fdir