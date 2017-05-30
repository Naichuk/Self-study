"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


def even_divisible():
    r = (2, 3, 5, 7, 11, 13, 17, 19)
    start = 2420
    while True:
        num = [x for x in r if start % x == 0]
        if len(num) == 8:
            return start
        start += 10