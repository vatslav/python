'''
рабин миилер тест, помоуйму этот не рабочий
'''


import random

def toBinary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
        return r
 
def MillerRabin(n, s = 50): 
    for j in range(1, s + 1):
            a = random.randint(1, n - 1)
            b = toBinary(n - 1)
            d = 1
            for i in range(len(b) - 1, -1, -1):
                x = d
                d = (d * d) % n
                if d == 1 and x != 1 and x != n - 1:
                    return True # compasite
                if b[i] == 1:
                    d = (d * a) % n
                    if d != 1:
                        return True # compasite
                    return False # simple
print(toBinary(2342342342342345490))


for x in range(3,33):
    if not MillerRabin(x):
        print(x,MillerRabin(x))