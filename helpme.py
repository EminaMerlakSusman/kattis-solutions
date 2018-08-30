import sys

'''Prejme ASCII art šahovnico, in izpiše, na katerih mestih so bele in črne figure.'''
#stolpci so črke, vrstice so številke, ki se štejejo od spodaj navzgor
stolpci = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h'}

bele = []  #velike črke
črne = [] #male črke

for i in range(17): #branje vrstic
    vrstica = sys.stdin.readline()
    if vrstica[0] == '|': #zanimajo nas samo tiste vrstice ki imajo opise figur
        vrstica = vrstica.split('|')[1:-1]
        for j in range(len(vrstica)):
            polje = stolpci[j] #črka polja
            vrs = 8 - (i // 2) #od spodaj navzgor index vrstice
            figura = vrstica[j][1]
            if figura.isalpha(): #če je figura črka
                if figura.isupper():
                    if figura != 'P':
                        bele.append(figura + polje + str(vrs))
                    else:
                        bele.append(polje + str(vrs))
                else:
                    if figura != 'p':
                        črne.append(figura.upper() + polje + str(vrs))
                    else:
                        črne.append(polje + str(vrs))

'''urejanje seznamov belih in črnih, tako da so oblike:
kralj, kraljica, rook, bishop, knight, kmet.'''                      

'''najprej sestavimo sezname za vsako figuro posebej,
nato pa vsak seznam posebej sortamo.
na koncu staknemo vse sezname skupaj.'''

beli_kralji = [fig for fig in bele if fig[0] == 'K']
bele_kraljice = [fig for fig in bele if fig[0] == 'Q']
bele_trdnjave = [fig for fig in bele if fig[0] == 'R']
beli_bishop = [fig for fig in bele if fig[0] == 'B']
beli_knight = [fig for fig in bele if fig[0] == 'N']
beli_kmetje = [fig for fig in bele if len(fig) == 2]

bele_figure = [beli_kralji, bele_kraljice, bele_trdnjave, beli_bishop, beli_knight, beli_kmetje]
for sez in bele_figure: #lambda vrne par (št_vrstice, črka_stolpca)
    sez.sort(key = lambda fig : (fig[-1], fig[-2])) #sorta po številki vrstice, če pa sta dve vrstici isti, ju še sorta po stolpcu
    
črni_kralji = [fig for fig in črne if fig[0] == 'K']
črne_kraljice = [fig for fig in črne if fig[0] == 'Q']
črne_trdnjave = [fig for fig in črne if fig[0] == 'R']
črni_bishop = [fig for fig in črne if fig[0] == 'B']
črni_knight = [fig for fig in črne if fig[0] == 'N']
črni_kmetje = [fig for fig in črne if len(fig) == 2]

črne_figure = [črni_kralji, črne_kraljice, črne_trdnjave, črni_bishop, črni_knight, črni_kmetje]
for sez in črne_figure:
    sez.sort(key = lambda fig : (fig[-1]), reverse = True) #sorta vrstice v obratnem vrstnem redu

#staknemo skupaj vse sezname
bele_urejeno = []
črne_urejeno = []

for sez in bele_figure:
    bele_urejeno += sez
for sez in črne_figure:
    črne_urejeno += sez

#tiskanje rešitev
print('White: ' + ','.join(bele_urejeno))
print('Black: ' + ','.join(črne_urejeno))