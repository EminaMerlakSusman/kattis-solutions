testi = int(input())
for i in range(testi):
    sum, diff = tuple(map(int, input().split()))
    a = (sum + diff)/2
    b = (sum - diff) / 2
    if b >= 0 and (b == int(b) and a == int(a)):
        print(int(a), int(b))
    else:
        print('impossible')