from django.utils import importlib
import unittest

def test_main():
    name = 'tests'
    test_module(name)

def test_module(mod_name):
    module = importlib.import_module(mod_name)
        
    print "Testing module: %s" %mod_name
    loader = unittest.TestLoader()
    suite  = loader.loadTestsFromModule(module)
    runner = unittest.TextTestRunner()
    runner.run(suite)

    

if __name__ == '__main__':
    test_main()