#class NoneRelase(Exception):
'''
автор: Вацлав
реализация алоритма шифровния RSA
'''
import random
import math
class rsa:
	
	_word = ''

	bitSize = 10
	e = 29
	n=0
	d=0
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
		return self.binpow(self.intcode, self.e, self.n)
		#return "encode was note define"
	def decode(self, output):
		text = self.binpow(output, self.d, self.n)
		print('decode: ',text)
		text = self._intToText(text)
		return text
	def binpow(self,a, x, mod):
	    #return math.pow(a,x) % mod
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
	def rabin_miller(self, m=bitSize, r=10):
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
	    return True
	def _primeGenerator(self,bitSize):
		'''генерирует простое случайное число заданной длины

		'''
		start = 2**(bitSize-1)
		end   = 2**bitSize - 1
		ptr = 0
		while (1):
		    prime = random.randint(start, end)
		    ptr+=1
		    #print(ptr)
		    if self.rabin_miller(prime):
		    	return prime
	def gcdExt(self,a,b):
		'''
		алгоритм нахождения расширенного алгоритма Евклида
		возвращает картеж из: d - НОД, x, y из 
		ax + by = НОД(a, b)
		'''
		x=y=d=0
		if b==0:
			x=1
			y=0
			return a,x,y


		d,x,y = gcdExt(b,a%b)
		x,y = y, x - (a/b) * y
		return d,x,y


	def keyGenerator(self):
		while 1:
			p = self._primeGenerator(self.bitSize) #генерируем p .1
			q = self._primeGenerator(self.bitSize) #генрируем q .1
			self.n = p * q #-||- q .2
			phi_n = (p-1) * (q-1) #.3
			if p!=q and phi_n > self.e and phi_n % self.e != 0: #.4
				break 
		self.d = math.pow(self.e,-1) % ((p-1)*(q-1))
		#e,n - open key, d - private key
		print(self.n,self.d)

'''
1)декод возврщаетет 1
'''





def main():
	myrsa = rsa()
	print(myrsa._textToint("hello world"))
	print(myrsa.rabin_miller(21, 3))
	myrsa.keyGenerator()
	print('hello: ',myrsa.encode("he"))
	print("dehello:",myrsa.decode(myrsa.encode("he")))


if __name__ == "__main__":
	main()
	import doctest
	doctest.testmod()
	
