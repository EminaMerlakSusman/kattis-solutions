n = int(input())
while n != 0:
    tab = []
    for i in range(n):
        time = input().split()
        t = time[0].split(':')
        hour = int(t[0])
        if time[1] == 'p.m.' and hour != 12:
            hour += 12
        elif hour == 12 and time[1] != 'p.m.':
            hour = 0
        minute = int(t[1])
        timeConvert = hour*60 + minute
        tab.append([timeConvert, time])
    seq = (sorted(tab))
    for list in seq:
        print(list[1][0] + " " + list[1][1])
    print('\n')
    n = int(input())
