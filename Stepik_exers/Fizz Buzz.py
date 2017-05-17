"""Sample Input:
8 16
Sample Output:
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16"""

def FizzBuzz(n,m):
        for i in range(n,m+1):
            if i % 3 == 0 and i % 5 == 0:
                print ('FizzBuzz')
            elif i % 5 == 0:
                print ('Buzz')
            elif i % 3 == 0:
                print('Fizz')
            else:
                print(i)