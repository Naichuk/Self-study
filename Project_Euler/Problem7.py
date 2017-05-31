"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
       d += 2
    return d * d > n

def problem7(data):
    res = [2]
    n = 3
    while True:
        if isPrime(n):
            res.append(n)
        if len(res)==len(range(data)):
            break
        n+=2
    return res[-1]