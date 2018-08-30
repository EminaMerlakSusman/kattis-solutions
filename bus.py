t = int(input())
for i in range(t):
    k = int(input())
    n = 0
    for i in range(k):
        n += 0.5
        n *= 2
    if k == 1:
        print(1)
    else:
        print(int(n))