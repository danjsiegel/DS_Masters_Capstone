import unittest
import datetime

from msds510.utils.date import *


class dateMethods(unittest.TestCase):

    def setUp(self):
        self.month = 'Oct'
        self.year = '2018'
        self.today = datetime.datetime.now().date()

    def test_getmonth_bad(self):
        self.assertEqual(getmonth('Bad Month'), 1)

    def test_getmonth_good(self):
        self.assertEqual(getmonth(self.month), 10)

    def test_getmonth_no_month(self):
        with self.assertRaises(TypeError):
            month = getmonth()

    def test_bad_datediffcalc(self):
        self.assertIsNone(datediffcalculator('sdfsdf'))

    def test_datediffcal(self):
        self.assertTrue(type(datediffcalculator(self.today)) == datetime.timedelta)

    def test_getDJ_good(self):
        self.assertEqual(str(getDJ(self.month, self.year)), '2018-10-01')

    def test_getDJ_bad_month(self):
        self.assertEqual(str(getDJ('sdfsdfsd', self.year)), '2018-01-01')

    def test_to_int_str(self):
        self.assertEqual(to_int('11'), 11)

    def test_to_int_float(self):
        self.assertEqual(to_int(11.6), 11)

if __name__ == '__main__':
    unittest.main()
