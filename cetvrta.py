xTab = []
yTab = []
for i in range(3):
    koord = input().split()
    x = int(koord[0])
    y = int(koord[1])
    xTab.append(x)
    yTab.append(y)
for x in xTab:
    if xTab.count(x) == 1:
        print(x, end = ' ')
for y in yTab:
    if yTab.count(y) == 1:
        print(y)