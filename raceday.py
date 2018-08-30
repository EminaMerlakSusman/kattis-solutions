import sys
class Tekač():
    '''Predstavi enega tekača.'''
    def __init__(self, ime, priimek, bib):
        '''Predstavi tekačevo ime, priimek in bib številko.'''
        self.ime = ime
        self.priimek = priimek
        self.bib = bib
        self.časi = {'S1' : '00:00', 'S2' : '00:00', 'F' : '00:00'}
        self.mesta = {'S1' : 0, 'S2' : 0, 'F' : 0}
    def pretvori(self):
        '''Vse čase pretvori v sekunde in vrne slovar s temi časi v posameznih etapah.'''
        časi = {'S1' : 0, 'S2' : 0, 'F' : 0}
        for etapa, čas in self.časi.items():
            pos = čas.split(':')
            min = int(pos[0])
            sek = int(pos[1])
            časi[etapa] = min * 60 + sek
        return časi
    def nastavi_rank(self, del_tekme, seznam_časov):
        '''Izračuna tekačev rank v določenem delu tekme na podlagi urejenega seznama seznam_časov.'''
        self.mesta[del_tekme] = seznam_časov.index(self.pretvori()[del_tekme]) + 1
    def __str__(self):
        '''Predstavi tekača v obliki: Priimek, Ime, bib, čas s1, rank s1, čas s2, rank s2, čas f, rank f.'''
        return '{}{}{}{}{}{}{}{}'.format('{}, {}'.format(self.priimek, self.ime).ljust(20), self.bib.rjust(10), self.časi['S1'].rjust(10), str(self.mesta['S1']).rjust(10), self.časi['S2'].rjust(10), str(self.mesta['S2']).rjust(10), self.časi['F'].rjust(10), str(self.mesta['F']).rjust(10))

##bert = Tekač('Bert', 'Trista', '00227')
##
##bert.časi['F'] = '52:41'
##print(bert.pretvori())
##print(bert.nastavi_rank('F', sorted([3161, 3300, 3162])))
##print(bert.mesta)
##print(bert)

def funkcija(n):
    '''Poskrbi, da se tole izvede n-krat.'''
    slovar_tekačev = {} #ključi so bib numberji, vrednosti pa objekti tipa Tekač
    slovar_časov = {} #ključi so imena etap, vrednosti pa seznami časov posameznih tekačev v tej etapi
    for _ in range(n):
        '''Prebiramo imena in delamo objekte tipa tekač ter jih spravljamo v slovar tekačev.'''
        sez = sys.stdin.readline().split()
        tekač = Tekač(sez[0], sez[1], sez[2])
        slovar_tekačev[tekač.bib] = tekač #bib number rabimo zato, ker bomo kasneje iskali tekače glede na bib numberje

    for _ in range(3*n):
        '''Prebiramo opise z bib št, etapo in časom.'''
        opis = sys.stdin.readline().split()
        bib = opis[0]
        etapa = opis[1]
        čas = opis[2]
        pret = čas.split(':')
        v_sek = int(pret[0]) * 60 + int(pret[1])
        #poiščemo tekača s to bib številko in posodobimo njegov čas v ustrezni etapi
        ustrezni_tekač = slovar_tekačev[bib]
        ustrezni_tekač.časi[etapa] = čas
        #čas v sekundah dodajamo v slovar časov
        if etapa in slovar_časov.keys():
            slovar_časov[etapa].append(v_sek)
        else:
            slovar_časov[etapa] = [v_sek]

    #zdaj ko imamo narejen seznam vseh časov za vsako etapo, še izračunamo rank vsakega tekača
    for tekač in slovar_tekačev.values():
        tekač.nastavi_rank('S1', sorted(slovar_časov['S1']))
        tekač.nastavi_rank('S2', sorted(slovar_časov['S2']))
        tekač.nastavi_rank('F', sorted(slovar_časov['F']))

    sez_tekacev = list(slovar_tekačev.values())
    sez_tekacev = sorted(sez_tekacev, key = lambda tekač : (tekač.priimek, tekač.ime)) #seznam sortamo glede na priimke
    print('NAME'.ljust(20) + 'BIB'.rjust(10) + 'SPLIT1'.rjust(10) + 'RANK'.rjust(10) + 'SPLIT2'.rjust(10) + 'RANK'.rjust(10) + 'FINISH'.rjust(10) + 'RANK'.rjust(10))
    for tekac in sez_tekacev:
        print(tekac)
    print('')

n = int(sys.stdin.readline())
while n != 0:
    funkcija(n)
    n = int(sys.stdin.readline())