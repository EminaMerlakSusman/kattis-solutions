import math
import sys

n = sys.stdin.readline()
while n != '':
#    print(int(math.log10(math.factorial(int(n)))) + 1)
    n = int(n)
    if n == 0 or n == 1:
        print(1)
    else:
        print(math.floor((math.log(2*math.pi*n)/2 + n*(math.log(n) - math.log(math.e)))/math.log(10)) + 1)
    n = sys.stdin.readline()
