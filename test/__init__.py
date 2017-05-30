import unittest
from .env import package_path

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('test', pattern='test_*.py')
    return test_suite

