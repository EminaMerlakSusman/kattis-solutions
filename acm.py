inpt = input().split()
time = 0
napacni = []
reseni = 0
while inpt != ['-1']:
    if inpt[2] == 'right':
        reseni += 1
        time += int(inpt[0]) + 20*napacni.count(inpt[1])
    elif inpt[2] == 'wrong':
        napacni.append(inpt[1])
    inpt = input().split()
print(reseni, time)