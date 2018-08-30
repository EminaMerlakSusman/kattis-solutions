t = int(input())

for i in range(t):
    s = list(map(int, input().split()))
    N = s[0]
    scores = s[1:]
    avg = sum(scores)/N
    f = list(filter(lambda x: x > avg, scores))
    above_avg = len(f)
    print('{:.3f}%'.format((above_avg/N)*100))
