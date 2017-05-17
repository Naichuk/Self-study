#Sample Input:
#15.5 mile in km
#Sample Output:
#2.49e+01

def Length_Translator():
    etalon = dict(mile=1609, yard=0.9144, foot=0.3048, inch=0.0254, km=1000, cm=0.01, mm=0.001, m=1)
    data = input().split()
    res = float(data[0]) * etalon[data[1]]/etalon[data[3]]
    print('{:.2e}'.format(res))