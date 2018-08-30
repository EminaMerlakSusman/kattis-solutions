line = list(map(int, input().split()))
while line != [0, 0]:
    if sum(line) == 13:
        print('Never speak again.')
    elif line[0] > line[1]:
        print('To the convention.')
    elif line[0] < line[1]:
        print('Left beehind.')
    elif line[0] == line[1]:
        print('Undecided.')
    line = list(map(int, input().split()))
