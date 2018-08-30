import sys

n = int(sys.stdin.readline())

for i in range(n):
    '''Prebere število in za vsakega pogleda najbližji palindrom.'''
    število = int(sys.stdin.readline())
##    j = stevilo
##    while str(j)[:3] != str(j)[3:][::-1]: #dokler st ni na obeh straneh isto, ga odstevas
##        j -= 1
##    print(j)
    najbližje = 0
    for j in range(100, 1000):
        sestavljeno = int(str(j) + str(j)[::-1])
        razd = abs(sestavljeno -število)
        if razd < abs(število - najbližje): #če je to število bližje, kot prejšnje
            najbližje = sestavljeno
    print(najbližje)