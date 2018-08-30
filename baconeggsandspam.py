n = int(input())

while n != 0:
    sestavine = {}
    for i in range(n):
        niz = input().split()
        ime = niz[0]
        sest = niz[1:]
        for jed in sest:
            if jed not in sestavine:
                sestavine[jed] = ime
            else:
                sestavine[jed] += ' ' + ime
    #output
    urejen_sestavine = sorted(sestavine.keys())
    for key in urejen_sestavine:
        urejena_imena = ' '.join(sorted(sestavine[key].split()))
        print(key, urejena_imena)
    print('\n')
    n = int(input())