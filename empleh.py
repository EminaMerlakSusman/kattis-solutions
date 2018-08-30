'''Dobi opis položajev šahovskih figur, in izpiše šahovnico.'''
import sys

plusi = '+---'*8 + '+' #vmesne vrstice s plusi

beli = sys.stdin.readline()[7:-1].split(',') #opis belih figur
črni = sys.stdin.readline()[7:-1].split(',') #opis črnih figur

stolpci = {'a': 0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7} #prevod iz stolpcev na številke

šahovnica = [['...', ':::', '...', ':::', '...', ':::', '...', ':::'], [':::', '...', ':::', '...', ':::', '...', ':::', '...'], ['...', ':::', '...', ':::', '...', ':::', '...', ':::'], [':::', '...', ':::', '...', ':::', '...', ':::', '...'], ['...', ':::', '...', ':::', '...', ':::', '...', ':::'], [':::', '...', ':::', '...', ':::', '...', ':::', '...'], ['...', ':::', '...', ':::', '...', ':::', '...', ':::'], [':::', '...', ':::', '...', ':::', '...', ':::', '...']]
if beli != ['']: #če navodila niso prazen niz
    for niz in beli:
        if len(niz) == 3:
            fig = niz[0].upper() #ime figure
            stolpec = stolpci[niz[1]] #št. stolpca
            vrst = 7 - (int(niz[2]) - 1) #št. vrstice
        else:
            fig = 'P' #kmetje nimajo spredaj črke
            stolpec = stolpci[niz[0]]
            vrst = 7 - (int(niz[1]) - 1) #vrstice so od spodaj gor oštevilčene
        #zgornjo šahovnico spremenimo tam, kjer so koordinate figure
        if (vrst % 2 == 0 and stolpec % 2 == 0):
            šahovnica[vrst][stolpec] = '.' + fig.upper() + '.'
        elif (vrst % 2 == 1 and stolpec % 2 == 0):
            šahovnica[vrst][stolpec] = ':' + fig.upper() + ':'
        elif (vrst % 2 == 0 and stolpec % 2 == 1):
            šahovnica[vrst][stolpec] = ':' + fig.upper() + ':'
        elif (vrst % 2 == 1 and stolpec % 2 == 1):
            šahovnica[vrst][stolpec] = '.' + fig.upper() + '.'
if črni != ['']: #če navodila niso prazen niz
    #naredimo še enkrat isto kot za bele figure
    for niz in črni:
        if len(niz) == 3:
            fig = niz[0]
            stolpec = stolpci[niz[1]]
            vrst = 7 - (int(niz[2]) - 1)
        else:
            fig = 'P'
            stolpec = stolpci[niz[0]]
            vrst = 7 - (int(niz[1]) - 1) #vrstice so od spodaj gor oštevilčene
        if (vrst % 2 == 0 and stolpec % 2 == 0):
            šahovnica[vrst][stolpec] = '.' + fig.lower() + '.'
        elif (vrst % 2 == 1 and stolpec % 2 == 0):
            šahovnica[vrst][stolpec] = ':' + fig.lower() + ':'
        elif (vrst % 2 == 0 and stolpec % 2 == 1):
            šahovnica[vrst][stolpec] = ':' + fig.lower() + ':'
        elif (vrst % 2 == 1 and stolpec % 2 == 1):
            šahovnica[vrst][stolpec] = '.' + fig.lower() + '.'

for sez in šahovnica:
    print(plusi) #na vrhu vsake vrstice plusi
    print('|', end = '') #začetni |
    print('|'.join(sez), end = '')
    print('|') #konec vrstice
print(plusi) #še na koncu plusi
    



