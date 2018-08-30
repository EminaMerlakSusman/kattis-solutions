import math

t = int(input())
for i in range(t):
    l = list(map(float, input().split()))
    D = l[0]
    d = l[1]
    s = l[2]
    print(math.floor(math.pi / math.asin((s + d) / (D -d))))