import sys

'''Pošlje matriko, ki opisuje sliko skozi matriko, ki opisuje kernel.'''

slika = []
kernel = []

dimenzije = sys.stdin.readline().split()
visinaSlike = int(dimenzije[0]) #h
sirinaSlike = int(dimenzije[1]) #w
visinaKer = int(dimenzije[2]) #m
sirinaKer = int(dimenzije[3]) #n

#sestavljanje slike:
for i in range(visinaSlike):
    vrstica = sys.stdin.readline().rstrip().split()
    vrsticaInt = list(map(int, vrstica))
    slika.append(vrsticaInt)

#sestavljanje kernela:
for i in range(visinaKer):
    vrstica = sys.stdin.readline().rstrip().split()
    vrsticaInt = list(map(int, vrstica))
    kernel.append(list(reversed(vrsticaInt))) #za lažje računanje že v štartu zamenjamo stolpce

kernel = list(reversed(kernel)) #sedaj pa še zamenjamo vrstice

#matrike, ki jih množimo:
matrike = [] #najprej se premikamo po vrsticah

k = 0
while k <= visinaSlike - visinaKer:
    '''najprej vzamemo prvih n stoplcev, od 0-tega do m-tega indeksa.
    nato prvih n stolpcev od 1-ega do m + 1-ega indeksa,
    ...itd, dokler ne pridemo do zadnjega bloka m stolpcev.
    nato vzamemo od 1-ega do m+1-ega stolpca - in isti postopek, dokler ne pridemo
    do zadnjega bloka po n vrstic.'''
    j = 0
    while j <= sirinaSlike - sirinaKer:
        matrika = []
        for i in range(visinaKer): #n-krat appendamo vrstico do m-tega elementa
            matrika.append(slika[i + k][j:sirinaKer+j]) #potem pa m-je zamikamo
        matrike.append(matrika)
        j += 1
    k += 1

##for vrs in matrike:
##    print(vrs)
##for vrs in kernel:
##    print(vrs)

#računanje matrike po kernelu
rezultat = []
for vrs in matrike:
    vsota = 0
    for i in range(len(vrs)):
        vrstica = vrs[i]
        zaRač = kernel[i]
        for j in range(len(vrstica)):
            vsota += vrstica[j]*zaRač[j]
    rezultat.append(vsota)

#k je tisti števec od prej, pove nam, kolikokrat smo
#se morali premakniti dol po matriki.
for i in range(0, len(rezultat), k):
    sez = rezultat[i:i+k]
    for j in range(len(sez) - 1):
        print(sez[j], end = ' ')
    print(sez[-1])
        
    
    
    