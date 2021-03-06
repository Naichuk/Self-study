"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def largest_prime(data, i = 2):
    while i < data:
        if data%i != 0:
            i += 1
        else:
            data = data/i
    return i