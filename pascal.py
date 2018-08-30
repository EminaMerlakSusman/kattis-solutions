import sys
import math
def readln(n):
    '''Vrne razliko med n-jem in njegovim največjim deliteljem, manjšim on n-ja.'''
    i = 2
    if n == 1:
        return 0
    while i != int(math.sqrt(n)) + 1: #hitreje je iti samo do korena števila, 'inverzni' delitelj pa je n // i
        if n % i == 0: #ko najdemo delitelj
            return n - n//i #njegov 'inverz' odštejemo od n
        i += 1
    if i == int(math.sqrt(n)) + 1: #če je n praštevilo
        return n - 1 
n = sys.stdin.readline()
while n != '':
    print(readln(int(n)))
    n = sys.stdin.readline()