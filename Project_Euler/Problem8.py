"""Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
What is the value of this product?"""


f=open('data.txt')
pre_res = 1
res = 0
i = 0
data = []
result = []
with open ('data.txt')as f:
    for line in f:
        data += line
data = [int(x) for x in data if x != '\n']
print (data)
while len(data)>13:
    count = 1
    for item in range(0,13):
        count *= data[item]
    result.append(count)
    data.pop(0)

print(max(result))