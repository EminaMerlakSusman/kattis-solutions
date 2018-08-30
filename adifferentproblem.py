import sys
from functools import reduce
n = sys.stdin.readline().split()
while n:
    print(reduce(lambda x, y: abs(x - y), map(int, n)))
    n = sys.stdin.readline().split()

