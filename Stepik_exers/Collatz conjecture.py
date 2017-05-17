#Sample Input 1:
#17
#Sample Output 1:
#17 52 26 13 40 20 10 5 16 8 4 2 1

def Collatz(num):
    while num != 1:
        if num %2 ==0:
            num = num//2
        else:
            num = num*3 +1
    print (num, end = ' ')
