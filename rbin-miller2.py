import random

def RabinMiller(n, k):

    # obviously not prime
    if n < 2 or n % 2 == 0:
        return False

    # special case        
    if n == 2:
        return True

    s = 0
    r = n - 1

    # factor n - 1 as 2^(r)*s
    while r % 2 == 0:
        s = s + 1
        r = r // 2  # floor

    # k = accuracy
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

print(RabinMiller(21, 500))