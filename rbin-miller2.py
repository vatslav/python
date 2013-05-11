import random

def RabinMiller(n, k):

    # еслинам дали число <2 или четное число
    if n < 2 or n % 2 == 0:
        return False

    # special case        
    if n == 2:
        return True

    s = 0
    r = n - 1

    # педставление n - 1 как 2^(r) * s
    while r % 2 == 0:
        s = s + 1
        r = r // 2  # целочисленное деление

    # k - точность
    for i in range(k):
        a = random.randrange(1, n)

        # a^(s) mod n = 1?
        if pow(a, s, n) == 1:
            return True

        # a^(2^(j) * s) mod n = -1 mod n?
        for j in range(r):
            if pow(a, 2**j*s, n) == -1 % n:
                return True

    return False
#print(RabinMiller(9,1000))
'''
for x in range(33):
    simple = RabinMiller(x, 1)
    hard = RabinMiller(x, 250)
    print(x, simple, hard, ["!!!",""][simple==hard])

'''

def binpow(a, x, mod):
    res = 1 #инициализуремпеременнюу под результат
    a %= mod #берем остаток от деления а на мод
    while (x): #пока x!=0
        #если х - нечетно
        if (int(x) & 1): #побитовое или при сравнение с 1 дает true если число нечетно
            res *= a
            res %= mod
        a *= a
        a %= mod
        x /= 2
    return res



bit = 20
def is_prime(num) :
    if (num == 2):
        return True
    if ((num < 2) or (num % 2 == 0)):
        return False
    b = 2
    p = 0
    q = num-1
    cnt = bit
    while (q % 2 == 0):
        q /= 2
        p += 1
    while (cnt):
        x = random.randint(1, num-1)
        x = binpow(x,q,num)
        if (x == 1 or x == num-1):
            return True
        for i in range(0,p):
            x = (x * x) % num
            if (x == num-1):
                break
            else:
                return False
            p -= 1
        cnt -= 1
    return False
#for x in range(0):
#    print(x, is_prime(x))

#print(151091, is_prime(151091)) 
'''
for x in range (2,20):
    for y in range(2,20):
        for z in range(2,20):
            a=binpow(x,y,z)
            if a!=0 and a!=1:
                print(a, x,y,z)
'''
def generateNumber(bit):
    '''
    генератор больших чисел заданной битности
    при генерирвоании маленьких чисел ведет себя плохо :)
    '''
    n=''
    for x in range(bit-2):
        if random.randint(0,1):
            n+="1"
        else:
            n+='0'
    #if bit>4:
    n = '1' + n + '1'
    res = int(n,2)
    return res

def simplePrime(n):
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

ptr=0
def isPrime(n):
    """
    >>> isPrime(165983)
    True
    >>> isPrime(165749)
    True
    >>> isPrime(165983)
    True
    >>> isPrime(165947)
    True
    >>> isPrime(11)#27511516267
    True
    >>> isPrime(6367)
    True
    """
    global ptr
    #есличетно
    if n<2 or n%2==0:
        return False
    #если меньше 256
    if n < 256:
        if simplePrime(n):
            return True
        else:
            return False
    #если делиться на числа в диапазоне:3...256
    for x in (3,255,2):
        if n%x==0:
            return False
    p = n-1 #пригодиться - нам часто нужно n-1
    b = 0 # сколько раз p делиться на 2
    while p%2==0:
        ptr = ptr + 1
        p /= 2
        b += 1
        #не ясносовсем почему тут так надо?! без этого дает неверный результат при
        #числах <100
    p = n - 1
    m = (n - 1 ) / (2**b)
    a = random.randint(2,p)

    j=0
    #z = (a**m) % n
    z = binpow(a,m,n)
    if z==1 or z==p:
        return True
    while (not (j>0 and z==1)):
        j+=1
        if j<b and z!=p:
            z = (z*z) % p
            break
        else:
        #if z==p:
            return True
    return False

def isPrimeExtra(n,k=1):
    if k<1:
        raise ValueError("lol accurasity")
    for i in range(k):
        if not isPrime(n):
            return False
    return True



if __name__ == '__main__':  
    #for x in range(3,51,2):`#165983
    #   print(x, isPrime(x))
    #x=449
    #print(isPrime(x))
    #print(simplePrime(x), ptr)
    import doctest
    doctest.testmod()
    print('finish')
    isPrimeExtra(165983,10)




#print(m, 1+(2**b)*m)







