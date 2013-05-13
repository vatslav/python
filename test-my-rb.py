import my_rb
import unittest
import random
#a = list(map(lambda:x*2, (for x,y in q))   )


class test_rsa(unittest.TestCase):
	"""юнитесты для RSA"""
	def setUp(self):
		'''инициализация '''
		self.tobject = my_rb.rsa()
		#self.assertEqual = ae
	def tearDown(self):
		''' финализатор'''
		pass
	def testTextToInt(self):
		t = self.tobject._textToint('hello world')
		self.assertEqual(t, 104101108108111032119111114108100)
	def testIntToText(self):
		t = self.tobject._intToText(104101108108111032119111114108100)
		self.assertEqual(t,'hello world')
	
	def testEncode(self):
		t = self.tobject.encode('hello word')
		#self.assertEqual(t, None)
	def testDecode(self):
		t = self.tobject.decode('123125436757687')
		#self.assertEqual(t, None)
	def smallPrimeVerificator(self,n):
	    i = 2
	    j = 0 # флаг
	    while i**2 <= n and j != 1:
	        if n%i == 0:
	            j = 1
	        i += 1
	    if j == 1:
	        return False
	    else:
	        return True
	def testPrimeGenerator(self):
		t = self.tobject._primeGenerator(5)
		self.assertEqual(self.smallPrimeVerificator(t),True)

		t = self.tobject._primeGenerator(40)
		self.assertEqual(self.smallPrimeVerificator(t),True)







		
if __name__ == '__main__':




	unittest.main()
