import my_rb
import unittest

#a = list(map(lambda:x*2, (for x,y in q))   )


class test_my_rb(unittest.TestCase):
	"""docstring for test_my_rb"""
	def __init__(self, arg):
		super(test_my_rb, self).__init__()
		self.arg = arg
	def setUp(self):
		tobject = my_rb.rsa()

	def testTextToInt(self):
		tobject._textToint('hello world1')
		self.assertEqual(104101108108111032119111114108100)
	def testIntToText(self):
		tobject._intToText(104101108108111032119111114108100)
		self.assertEqual('hello world')
		
if __name__ == '__main__':
	unittest.main()