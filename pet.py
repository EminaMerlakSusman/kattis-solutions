max, j = (0, 1)
for i in range(5):
    l = map(int, input().split())
    score = sum(l)
    if score > max:
        max, j = score, i + 1
print(j, max)