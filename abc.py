l = map(int, input().split())
l = sorted(l)
A = l[0]
B = l[1]
C = l[2]
str = input()

for i in str:
    if i == 'A':
        print(A, end = ' ')
    elif i == 'B':
        print(B, end = ' ')
    else:
        print(C, end = ' ')