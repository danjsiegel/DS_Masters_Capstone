import unittest
from msds510.avenger import *


class AvengerMethods(unittest.TestCase):

    def setUp(self):
        self.test_record = {
            'appearances': '1269',
            'current': 'YES',
            'death1': 'YES',
            'death2': '',
            'death3': '',
            'death4': '',
            'death5': '',
            'full_reserve_avengers_intro': 'Sep-63',
            'gender': 'MALE',
            'honorary': 'Full',
            'name_alias': 'Henry Jonathan "Hank" Pym',
            'notes': 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n',
            'probationary_introl': '',
            'return1': 'NO',
            'return2': '',
            'return3': '',
            'return4': '',
            'return5': '',
            'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)',
            'year': '1963',
            'years_since_joining': '52'
        }
        self.test_class = Avenger(self.test_record)

    def test_return_dict_is_dict(self):
        returned_dict = self.test_class.return_dict()
        self.assertTrue(type(returned_dict) == dict)

    def test_url(self):
        self.assertIsNotNone(self.test_class.name_alias())

    def test_appearances(self):
        self.assertTrue(type(self.test_class.appearances()) == int)

    def test_current_status(self):
        self.assertTrue(type(self.test_class.is_current()) == bool)

    def test_gender(self):
        self.assertIn(self.test_class.gender(), ['MALE', 'FEMALE'])

    def test_year(self):
        self.assertTrue(type(self.test_class.year()) == int)

    def test_date_j(self):
        self.assertTrue(str(self.test_class.date_joined()) == '1963-09-01')

    def test_days_j(self):
        self.assertTrue(type(self.test_class.days_since_joining()) == int)

    def test_years_j(self):
        self.assertTrue(type(self.test_class.years_since_joining()) == int)

    def test_notes(self):
        self.assertTrue(type(self.test_class.notes()) == str)

    def test__str__(self):
        testStr = self.test_class.name_alias()
        self.assertEqual(testStr, self.test_class.__str__())

    def test__repr__(self):
        testRpr = 'Avenger(name_alias=Henry Jonathan "Hank" Pym, url=http://marvel.wikia.com/Henry_Pym_(Earth-616))'
        self.assertEqual(testRpr, self.test_class.__repr__())

    def test_avenger_records(self):
        with self.assertRaises(TypeError):
            test_record = Avenger()

if __name__ == '__main__':
    unittest.main()

