#class NoneRelase(Exception):

q = '123456'
print([lambda x:  for x in range(len(q))])



class rsa:
	_intTextList = [] # crypt word in number
	_word = ''
	def __init__(self,word):
		self.word = word
	def __init__(self):
		pass

	def _textToint(self,word):
		s = [ord(x) for x in word]
		s = ''.join(map(lambda x:str(x)+" ",s)  )
		s = s[0:-1]
		return s
		

	def _intToText(self, intTextList):
		return ''.join(map(lambda x:chr(int(x)),intTextList.split(' ')))

	def _getB(number):
		b = 0
		number -= 1
		while number % 2 == 0:
			number /= 2
			b += 1
		return b
	def encode(self, inword):
		intTextList = _textToint(self._word)
		raise NameError("encode was none define")
		return None
	def decode(self, inCode):
		raise NameError("decode was none define")
		return None

class rsaTest:
	def __init__(self):
		self.rsa_main = rsa()
		word = "hello world"
	def generalTest(self):
		if self.rsa.decode(self.rsa-main.encode(word)) == word:
			return True
		return False
	def textToIntVerify(self):
		pass

myrsa = rsa()
print(rsaTest.generalTest())



'''
def getB2(number):
	b = 0
	number -= 1
	while number / 2 > 2:
		number /= 2
		b += 1
	return b	

p = 23
pLess = p - 1

b = getB(p)
t = pLess/2

bx = 2**b
print(b, (2**b)*t + 1, p/bx, b)

b = getB2(p)
bx = 2**b
print(b, (2**b)*(p/bx), p/bx, b)
'''