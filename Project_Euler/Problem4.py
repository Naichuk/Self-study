"""A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_polindrom(num):
    return str(num) == str(num)[::-1]

res=[]
for i in range(100,1000):
    for j in range(100,1000):
        if is_polindrom(i*j)==True:
            res.append(i*j)
print(max(res))