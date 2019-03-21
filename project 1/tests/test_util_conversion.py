import unittest
import sys

from msds510.utils.conversion import *


class UtilMethods(unittest.TestCase):
    def setUp(self):
        sys.argv.append('Test')
        self.header_to_fix = '  Appearances   '
        self.header_to_fix_2 = 'Name/Alias'
        self.bool_yes = 'YES'
        self.bool_no = 'NO'
        self.bool_other = 'asdfasdfasd'

    def test_argumentExists(self):
        self.assertEqual('Test', argumentExists(1))

    def test_blank_argumentExists(self):
        self.assertIsNone(argumentExists(45))

    def test_make_nice_name_no_replacements(self):
        fixed_header = make_nice_name(self.header_to_fix)
        for letter in fixed_header:
            self.assertTrue(letter.islower())
        self.assertTrue(fixed_header[0] != ' ')
        self.assertTrue(fixed_header[-1] != ' ')

    def test_make_nice_name_replacements(self):
        fixed_header = make_nice_name(self.header_to_fix_2)
        self.assertNotIn(fixed_header, '/')

    def test_make_nice_name_bad_arg(self):
        with self.assertRaises(TypeError):
            make_nice_name()

    def test_to_bool_y(self):
        self.assertTrue(to_bool(self.bool_yes))

    def test_to_bool_n(self):
        self.assertFalse(to_bool(self.bool_no))

    def test_to_bool_blank(self):
        self.assertIsNone(to_bool(self.bool_other))

if __name__ == '__main__':
    unittest.main()
