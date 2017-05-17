#Sample Input 1:
#1 -3 -4 -1 1
#Sample Output 1:
#Jolly
#Sample Input 2:
#1 3 5
#Sample Output 2:
#Not jolly

def JollyJumper():
    z = list(map(int,input().split()))
    print('Jolly' if sorted([abs(z[i]-z[i+1]) for i in range(len(z)-1)]) == list(range(1,len(z))) else 'Not jolly')