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
	m = 1024 
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

	def encode(self, inword):
		self.intcode = self._textToint(inword)
		#raise NameError("encode was note define")
		return "encode was note define"
	def decode(self, inCode):
		#raise NameError()
		return "decode was none define"
	def binpow(self,a, x, mod):
	    res = 1
	    a %= mod
	    while (x):
	        if (int(x) & 1):
	            res *= a
	            res %= mod
	        a *= a
	        a %= mod
	        x /= 2
	    return res
	def rabin_miller(self, m=m, r=10):
	    if (m == 2):
	        return True
	    if ((m < 2) or (m % 2 == 0)):
	        return False
	    p = 0
	    q = m-1
	    
	    #ищем степень в которую можно возвести
	    while (q % 2 == 0):
	        q /= 2
	        p += 1
	    #цикл A
	    while (r):
	        x = random.randint(2, m-1) # случайное число из диапазона
	        x = self.binpow(x,q,m) #то самое стремление к х
	        if (x == 1 or x == m-1):
	            return True
	        #цикл Б
	        for i in range(0,p):
	            x = (x * x) % m
	            if (x == m-1):
	                break
	            else:
	                return False
	            p -= 1
	        r -= 1
	    return False
	def primeGenerator(self,bitSize):
		'''генерирует простое случайное число заданной длины

		'''
		start = 2**(bitSize-1)
		end   = 2**bitSize - 1

		while (1):
		    prime = random.randint(start, end)
		    if self.rabin_miller(prime):
		    	return prime

	def keyGenerator(self):
		pass
    	




def main():
	myrsa = rsa()
	print(myrsa._textToint("hello world"))
	print(myrsa.rabin_miller(21, 3))


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	main()
