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
    res = 1
    a %= mod
    #print(type(x))
    while (x):
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
for x in range(33):
    print(x, is_prime(x))

print(151091, is_prime(151091))   

