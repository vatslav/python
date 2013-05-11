def f(a, b):
  '''
  Функция складывает два числа
  >>> f(1,2)
  3
  >>> f(2,3)
  5
  '''
  return a + b

def fact(n):
	'''
	функция нахождения факториала
	>>> fact(1)
	1
	>>> fact(5)
	120

	'''
	if n == 0 or n==1:
		return 1
	return n*fact(n-1)


if __name__ == '__main__':
  import doctest
  doctest.testfile('testTdd1.py')
  #doctest.testmod()
  