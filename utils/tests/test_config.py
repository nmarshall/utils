
import config
import os
from common import CommonTestCase


__all__ = ['TestConfigUnitTest',
           ]

class TestConfigUnitTest(CommonTestCase):
    
    config_fname = 'shortrules.conf'
    
    def test_config(self):
        fdir = self.fixture_dir()
        fname = os.path.join(fdir, self.config_fname)
        
        parser = config.RobustConfigParser(fname)
        result = parser.todict()
        self.assertTrue(isinstance(result, dict))
        
    