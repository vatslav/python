#рса с античата
#!/usr/bin/python
import random

def gcd(v1, v2):
    if (v2 == 0):
        return v1
    return gcd(v2, v1 % v2)

def euclid_ext(a,b):
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    q = 0
    r = 0
    if (b == 0):
        return 0
    while (b > 0):
        q = a/b
        r = a - q*b
        x = x2 - q*x1
        y = y2 - q*y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return y2

def binpow(a, x, mod):
    res = 1
    a %= mod
    while (x):
        if (x & 1):
            res *= a
            res %= mod
        a *= a
        a %= mod
        x /= 2
    return res

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

def generate(p1,p2):
    while (1):
        curr = random.randint(p1, p2)
        if (is_prime(curr)):
            return curr

def enc(input):
    return binpow(input, e, n)

def dec(output):
    return binpow(output, d, n)

####################
bit = 10
e = 3
msg = 6666
####################
d = 0
n = 0
start = 2**(bit-1)
end = 2**bit - 1

while (1):
    p = generate(start,end)
    q = generate(start,end)
    n = p*q
    phi_n = (p-1)*(q-1)
    if ((p != q) and (phi_n > e) and (phi_n % e != 0)):
        break
d = euclid_ext(phi_n, e)
d = ((d % phi_n) + phi_n) % phi_n
####################

print "RSA public key:\n{e, n} = {"+str(e)+", "+str(n)+"}\n"
print "RSA private key:\n{d, n} = {"+str(d)+", "+str(n)+"}\n"
print "Encoded message: "+str(enc(msg))
print "Decoded message: "+str(dec(enc(msg)))





