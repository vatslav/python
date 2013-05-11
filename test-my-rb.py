import my_rb
import unittest
import random
#a = list(map(lambda:x*2, (for x,y in q))   )


class test_my_rb(unittest.TestCase):
	"""docstring for test_my_rb"""
	def setUp(self):
		self.tobject = my_rb.rsa()
		#self.assertEqual = ae
	def tearDown(self):
		pass
	def testTextToInt(self):
		t = self.tobject._textToint('hello world')
		self.assertEqual(t, 104101108108111032119111114108100)
	def testIntToText(self):
		t = self.tobject._intToText(104101108108111032119111114108100)
		self.assertEqual(t,'hello world')
	def test_getS(self):
		#статичный тест
		t = self.tobject._getS(65)
		self.assertEqual(t, 6)
		#динамический тест
		for I in range(10):
			x = 2
			while (x-1) % 2 != 0:
				x = random.randint(3, 99999999)
			t = self.tobject.bVeify(x,self.tobject._getS(x))
			self.assertEqual(t, True)
		
		word = 'hello world'
		t = (self.tobject.decode(self.tobject.encode(word)) == word)
		#self.assertEqual(t,True)
	
	def testEncode(self):
		t = self.tobject.encode('hello word')
		#self.assertEqual(t, None)
	def testDecode(self):
		t = self.tobject.decode('123125436757687')
		#self.assertEqual(t, None)

	




		
if __name__ == '__main__':
	unittest.main()