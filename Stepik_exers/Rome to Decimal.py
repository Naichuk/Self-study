#Sample Input 1:
#MCMLXXXIV
#Sample Output 1:
#1984

def Rome_to_Dec(rome):
    dic1={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    dic2={'CM':900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
    res = 0
    for key in dic2:
        if key in rome:
            res += dic2[key]
            rome = rome.replace(key,'')
    print(res)
    print (rome)
    for key in rome:
        res += dic1[key]
    print(res)
