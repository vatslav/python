#class NoneRelase(Exception):
'''
автор: Вацлав
реализация алоритма шифровния RSA
'''


class rsa:
	_intTextList = [] # crypt word in number
	_word = ''
	def __init__(self,word):
		self.word = word
	def __init__(self):
		pass

	def _textToint(self,word):
		'''
		метод преобразования текста в соотвествующий код ascii & unicode
		работа отлаживается только на acii
		>>> a = rsa();a._textToint('hello world')
		104101108108111032119111114108100
		'''
		s = [ord(x) for x in word]
		s = ''.join(map(lambda x: [str(x),"0"+str(x)][x<100] ,s)  )#если код <100 подставить 0  в начало
		s = int(s)
		return s
		

	def _intToText(self, intcode):
		'''
		метод преобразования кода чисел в символы
		'''
		intcode = str(intcode)
		ptr=0
		buf = ''
		result = ''
		for x in range(len(intcode)):
			buf+=intcode[x]
			ptr+=1
			if ptr==3:
				ptr=0
				result+=chr(int(buf))
				buf=''

		return result

	def _getS(self,number):
		b = 0
		number -= 1
		while number % 2 == 0:
			number /= 2
			b += 1
		return b
	def _getT(self,m,t):
		return m/(2**t)
	def bVeify(self,m,b):
		m=m-1
		if (2**b)*(m/(2**b))==m:
			return True
		return False
	def encode(self, inword):
		intTextList = _textToint(self._word)
		raise NameError("encode was")
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
print(myrsa._textToint("hello world"))
#b=myrsa._getB(65)
#print(b, ))

if __name__ == "__main__":
	import doctest
	doctest.testmod()


def run_once(f):
    """
    Мемоизация. Не зависит от аргументов.
    """
    def _f(*args, **kwargs):
        if not hasattr(_f, "_retval"):
            _f._retval = f(*args, **kwargs)
        return _f._retval
    return _f

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