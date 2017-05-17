'''Sample Input 1:
silent
listen
Sample Output 1:
True
Sample Input 3:
abaca
acada
Sample Output 3:
False'''

def Anagrams():
    word1 = list(input('Input first word: ').lower())
    word2 = list(input('Input second word: ').lower())

    word1.sort()
    word2.sort()

    print(word1 == word2)