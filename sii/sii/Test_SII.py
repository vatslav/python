import random
import nbneibors
import unittest

class testClasters(unittest.TestCase):
	'''tests for SII'''
	def setUp(self):
		self.test = nbneibors.mdNeighbor()
	def tearDown(self):
		pass
	def test_d(self):
		#проверка растояния
		a = (1,1)
		b = (1,2)
		t = self.test.d(a,b)
		self.assertEqual(t,5)



if __name__ == '__main__':




	unittest.main()