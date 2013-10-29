
import unittest
from wyther.Wyther import Wyther, InvalidAppIdException

class WytherTests(unittest.TestCase):

	APP_ID = 'YOUR APP ID'

	def setUp(self):
		self.wyther = Wyther(self.APP_ID)

	def test_invalidappid(self):
		self.wyther = Wyther("somethingrandom")
		self.assertRaises(InvalidAppIdException,self.wyther.get_place_woeid,('atlanta','us'))
		self.assertRaises(InvalidAppIdException,self.wyther.by_place,('atlanta','us'))

	def test_invalidwoeid(self):
		pass

	def test_invalidplace(self):
		pass

if __name__ == '__main__':
    unittest.main()