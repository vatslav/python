import random
from sii3 import *
import unittest

class testClasters(unittest.TestCase):
	'''tests for SII3'''
	def setUp(self):
		pass
	def tearDown(self):
		'''complite test1'''
		pass
	def test_d(self):
		"""растояние между 2 точками"""
		a = (1,1)
		b = (1,2)
		c = (10,1)
		t1 = d(a,b)
		t2 = d(a,c)
		t3 = d(c,c)
		self.assertEqual(t1,1)
		self.assertEqual(t2,9)
		self.assertEqual(t3,0)
	def test_points(self):
		initPoints()
		




if __name__ == '__main__':




	unittest.main()