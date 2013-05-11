import splitter
import unittest

class TestSplitFunction(unittest.TestCase):
	"""docstring for TestSplitFunction"""
#	def __init__(self, arg):
#		super(TestSplitFunction, self).__init__()
#		self.arg = arg
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def testSimpleString(self):
		r = splitter.split('Goog 100 490.50')
		self.assertEqual(r,['Goog','100','490.50'])
	def testTypeConvert(self):
		r = splitter.split('Goog 100 490.50',[str,int,float])
		self.assertEqual(r,['Goog',100,490.50])
	def testDelimeter(self):
		pass
if __name__ == '__main__':
	unittest.main()