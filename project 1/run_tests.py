import unittest
from mock import patch
import sys
from tests import test_avenger, test_util_date, test_util_conversion

def doTests():
    suite = unittest.TestLoader().loadTestsFromModule(test_util_conversion)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromModule(test_util_date)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromModule(test_avenger)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    doTests()
