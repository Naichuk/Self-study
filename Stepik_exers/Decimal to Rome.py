#Sample Input 1:
#1984
#Sample Output 1:
#MCMLXXXIV

def Dec_to_Rome(number):
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rome = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""

    for i in range(len(arabic)):
        letter = number//arabic[i]
        if 0 < letter:
            result += rome[i] * letter
            number %= arabic[i]

    print(result)