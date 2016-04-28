import unittest
from wyther.Wyther import Wyther

class TestBasic(unittest.TestCase):

    def setUp(self):
        self.wyther = Wyther()

    def test_is_response_number_with_woeid(self):
        int(self.wyther.by_woeid(2442047))

    def test_is_response_number_with_place(self):
        int(self.wyther.by_place(('durham', 'nc')))

    def test_is_response_number_with_celcius_units(self):
        int(self.wyther.by_woeid(2442047, 'c'))
        int(self.wyther.by_place(('durham', 'nc')))

if __name__ == '__main__':
    unittest.main()
