num = int(input())
desc = list(map(int, input().split()))
sum = 0
n = 0
for i in desc:
    if i != -1:
        n += 1
        sum += i
print(sum/n)