import unittest
from city_functions import name
class NamesTest(unittest.TestCase):
    def test_name(self):
        formatted_name = name('Santiago','Chile')
        self.assertEqual(formatted_name,'Santiago,Chile')

unittest.main()