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
print(RabinMiller(29,100))

for x in range(33):
    simple = RabinMiller(x, 1)
    hard = RabinMiller(x, 250)
    print(x, simple, hard, ["!!!",""][simple==hard])



