import sys

'''Prebere ključ in niz ter vsak del niza, dolg n znakov,
zakriptira po tem ključu.'''

vrs = sys.stdin.readline().split()
while vrs != ['0']:
    n = int(vrs[0]) #dolžina permutacije
    permutacija = [int(i) for i in vrs[1:]] #ključ
    niz = sys.stdin.readline()[:-1]
    if len(niz) % n != 0: #če dolžina niza ni večkratnik dolžine permutacije
        niz += ' '*(n - len(niz) % n)
    deli = [niz[i:n+i] for i in range(0, len(niz), n)] #razdeli niz na n enako dolgih delov
    enkripcija = '\''
    for podniz in deli:
        for j in range(len(podniz)):
            enkripcija += podniz[permutacija[j] - 1]
    enkripcija += '\''
    print(enkripcija)
    vrs = sys.stdin.readline().split()
