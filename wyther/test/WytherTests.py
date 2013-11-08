
import unittest
from wyther.Wyther import *

class WytherTests(unittest.TestCase):

	APP_ID = 'APP ID'

	def setUp(self):
		self.wyther = Wyther(self.APP_ID)

	def test_normalcase(self):
		self.wyther.by_place(('atlanta','us'))
		self.wyther.by_place(('atlanta','us'),'c')
		self.wyther.by_woeid(2357024)
		self.wyther.by_woeid(2357024,'c')
		self.wyther.get_place_woeid(('atlanta','us'))

	def test_invalidappid(self):
		self.wyther = Wyther("somethingrandom")
		self.assertRaises(InvalidAppIdException,self.wyther.get_place_woeid,('atlanta','us'))
		self.assertRaises(InvalidAppIdException,self.wyther.by_place,('atlanta','us'))

	def test_invalidwoeid(self):
		self.assertRaises(InvalidWoeIdException,self.wyther.by_woeid,-1)
		self.assertRaises(InvalidWoeIdException,self.wyther.by_woeid,2.1)
		self.assertRaises(InvalidWoeIdException,self.wyther.by_woeid,None)
		self.assertRaises(InvalidWoeIdException,self.wyther.by_woeid,'')

	def test_invalidplace(self):
		self.assertRaises(InvalidPlaceException,self.wyther.by_place,('nowhere','nowhere'))
		self.assertRaises(InvalidPlaceException,self.wyther.by_place,'blahblah')

if __name__ == '__main__':
    unittest.main()