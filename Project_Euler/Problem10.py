"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
       d += 2
    return d * d > n

res = [x for x in range(0,2000001) if isPrime(x)]
print (sum(res)-1)