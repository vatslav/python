#class NoneRelase(Exception):
'''
автор: Вацлав
реализация алоритма шифровния RSA
'''
import random

class rsa:
	
	_word = ''
	s = 0
	t = 0
	m = 0 
	def __init__(self,word):
		self.word = word
	def __init__(self):
		self.m = 131
		self.s = self._getS()
		self.t = self._getT()

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

	def _getS(self,number=m):
		b = 0
		number -= 1
		while number % 2 == 0:
			number /= 2
			b += 1
		return b
	def _getT(self,m=m,s=s):
		return m/(2**s)
	def bVeify(self,m,b):
		m=m-1
		if (2**b)*(m/(2**b))==m:
			return True
		return False
	def encode(self, inword):
		self.intcode = self._textToint(inword)
		#raise NameError("encode was note define")
		return "encode was note define"
	def decode(self, inCode):
		#raise NameError()
		return "decode was none define"
	def rabin_miller(self, m=m, r=10):
		#A
		flag = False
		for i in range(r):
			a = random.randint(2, m-2)
			x = pow(a,self.t) % self.m
			
			if x==1 or x==self.m - 1:
				continue
			#B

			for j in range(self.s):
				x = (x*x) % self.m
				if x==1:
					return False # comlex
				if x==self.m-1:
					flag = True 
					break
			if flag==True:
				flag=False
				continue
			return False #complex
		return True #Simple



def main():
	myrsa = rsa()
	print(myrsa._textToint("hello world"))
	print(myrsa.rabin_miller(21, 3))


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	main()
