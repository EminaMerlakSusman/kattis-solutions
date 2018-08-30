import sys

'''Prebere podatke o doseženih točkah na turnirju tenisa in določi, ali so igre veljavne.'''

class Tenisač():
    '''Razred, ki opisuje enega tenisača.'''
    def __init__(self, ime):
        '''Prejme argumenta ime in število zmaganih iger.'''
        self.ime = ime
        self.zmage = 0
        self.zmaganih_setov = 0
    def __gt__(self, drugi):
        '''Primerja število zmag dveh tenisačev.
        Če eden zmaga več kot dve igri več od drugega in ima več kot 6 iger,
        je zmagovalec.'''
        return (self.zmage >= 6) and self.zmage - drugi.zmage >= 2
    def dodaj_zmage(self, x):
        self.zmage += x
        return self.zmage

##fedo = Tenisač('federer', 3)
##rodd = Tenisač('roddick', 6)
##print(max(fedo, rodd))

'''Set je neveljaven v naslednjih primerih:
1.	Set je izenačen
2.	Zmagovalec ima manj kot 6 iger
3.	Zmagovalec je zmagal set z razliko le ene igre (razen 7 : 6 v prvih dveh setih), ali pa več kot dvema igrama, če jih je zmagal 7.
4.	Zmagovalec je zmagal več kot 7 iger v prvem ali drugem setu
5.	Rezultat je 1 : 0, 1 : 1, ali pa 3 : 0, ali pa so bili odigrani več kot trije seti
6.	Federer je izgubil set
'''

'''Preveri, ali je tekma veljavna.
Vsakič ko naleti na kritičen pogoj, ustavi funkcijo in vrne 'ne'.'''
imeni = sys.stdin.readline().split() #branje imen
prvi = Tenisač(imeni[0])
drugi = Tenisač(imeni[1])
št_tekem = int(sys.stdin.readline()) #branje števila tekem
for t in range(2, št_tekem + 2):
    tekma = sys.stdin.readline().split() #informacije o posameznih setih
    #za vsak set posebej se izvede to spodi
    je_veljavna = True
    zmagovalcev = 0
    for i in range(len(tekma)):
        set = tekma[i]
        točke_prvi_drugi = set.split(':') #seznam, koliko točk je dosegel vsak
        prvi.dodaj_zmage(int(točke_prvi_drugi[0]))
        drugi.dodaj_zmage(int(točke_prvi_drugi[1]))
        if prvi.zmage > drugi.zmage:
            zmagovalec = prvi
            poraženec = drugi
        elif prvi.zmage < drugi.zmage:
            zmagovalec = drugi
            poraženec = prvi
        else:
            zmagovalec = prvi
            poraženec = drugi
        '''Pogoj 1.'''
        #dva igralca zmagala enako število setov  v igri
        zmagovalec.zmaganih_setov += 1
        if zmagovalec.zmage == poraženec.zmage:
            print('ne')
            je_veljavna = False
            prvi.zmage = 0
            drugi.zmage = 0
            break
        '''Pogoj 2.'''
        #če je zmagal set z manj kot 6-imi igrami
        if (zmagovalec.zmage < 6):
            print('ne')
            je_veljavna = False
            prvi.zmage = 0
            drugi.zmage = 0
            break
        '''Pogoj 3.'''
        #če je v tretjem setu zmagal tekmo z razliko samo 1
        if zmagovalec.zmage - poraženec.zmage == 1:
            if not (zmagovalec.zmage == 7 and poraženec.zmage == 6 and i in [0, 1]): #razen če je 7:6 v prvih dveh setih
                print('ne') #je set ilegalen
                je_veljavna = False
                prvi.zmage = 0
                drugi.zmage = 0
                break
        #če je zmagal 7 iger, potem ne sme biti razlika več kot 2
        if zmagovalec.zmage == 7 and zmagovalec.zmage - poraženec.zmage > 2:
            print('ne')
            je_veljavna = False
            prvi.zmage = 0
            drugi.zmage = 0
            break
        '''Pogoj 4.'''
        #če je igralec zmagal več kot 7 iger v prvem ali drugem setu
        if (zmagovalec.zmage > 7) and i in [0, 1]:
            print('ne')
            je_veljavna = False
            prvi.zmage = 0
            drugi.zmage = 0
            break
        '''Pogoj 5.'''
        #če je rezultat 0:1, 1:1 ali 3:0, ali če je bilo odigranih več kot 3 setov
        if set in ['1:0', '1:1' '3:0'] or len(tekma) > 3:
            print('ne')
            je_veljavna = False
            prvi.zmage = 0
            drugi.zmage = 0
            break
        '''Pogoj 6.'''
        #a je match igral Federer in izgubil?
        if prvi.ime == 'federer' or drugi.ime == 'federer':
            if 'federer' != zmagovalec.ime:
                print('ne')
                je_veljavna = False
                prvi.zmage = 0
                drugi.zmage = 0
                break
        #tekma se mora končat, če eden od igralcev zmaga vsaj 2 seta.
        if zmagovalec.zmaganih_setov == 2 and i != len(tekma) - 1: #pomeni, da imamo že zmagovalca, a se tekma še kar nadaljuje
            print('ne')
            je_veljavna = False
            prvi.zmage = 0
            drugi.zmage = 0
            break
        #če smo prišli do konca tekme brez da bi eden zmagal vsaj dva seta
        if zmagovalec.zmaganih_setov == 1 and i== len(tekma) - 1:
            print('ne')
            je_veljavna = False
            prvi.zmage = 0
            drugi.zmage = 0
            break
        prvi.zmage = 0
        drugi.zmage = 0
    if je_veljavna: #če smo prišli do konca zanke, brez da bi naprintal 'ne'
        print('da')
    prvi.zmaganih_setov = 0
    drugi.zmaganih_setov = 0
