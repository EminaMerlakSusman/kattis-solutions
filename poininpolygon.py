import sys
import math
class Točka():
    '''Predstavlja točko s koordinatama x in y.'''
    def __init__(self, niz):
        '''Dobi niz oblike 'x y' in iz njega razbere točkini koordinati.'''
        sez = niz.split()
        self.x = int(sez[0])
        self.y = int(sez[1])

    def je_na_črti(self, krajišče1, krajišče2):
        '''Preveri ali točka 'točka' leži na daljici med krajišče1 in krajišče2.'''
        #računanje razdalje med krajišče1 in krajišče2
        razd_krajišči = math.sqrt((krajišče1.x - krajišče2.x)**2 + (krajišče1.y - krajišče2.y)**2)
        #če je vsota razdalj točke od obeh krajišč enaka razdalji med krajiščema
        #potem ta točka leži na daljici.
        razd1 = math.sqrt((self.y - krajišče1.y)**2 + (self.x - krajišče1.x)**2) #med točko in krajišče1
        razd2 = math.sqrt((self.y - krajišče2.y)**2 + (self.x - krajišče2.x)**2) #med točko in krajišče2
        razd = razd1 + razd2
        return razd == razd_krajišči

def točka_v_poligonu(točka, poligon):
    števec = 0
    for i in range(len(poligon) - 1): #se sprehodimo po vseh stranicah v poligonu
        if toč.je_na_črti(poligon[i], poligon[i + 1]):
            return 'on'
        elif (poligon[i].y <= toč.y < poligon[i + 1].y) or (poligon[i + 1].y <= toč.y < poligon[i].y): #prečkanje oblike -/- ali -\-
            #iz točke spustimo žarek v desno in štejemo, kolikokrat seka mejo poligona
            raz = (toč.y - poligon[i].y) / (poligon[i + 1].y - poligon[i].y) #razmerje med obema y-onoma oglišč poligona
            #iz drugega oglišča se za 'raz' pomaknemo po x koordinati
            #da dobimo x-koordinato presečišča
            presečišče_x = poligon[i].x + raz * (poligon[i + 1].x - poligon[i].x)
            if toč.x < presečišče_x:
                števec += 1
    if števec % 2 == 0:
        return 'out'
    else:
        return 'in'       

n = int(sys.stdin.readline()) #število oglišč poligona
while n != 0:
    poligon = []
    for i in range(n):
        '''Branje koordinat poligona.'''
        toč = Točka(sys.stdin.readline())
        poligon.append(toč)

    poligon.append(poligon[0]) #zadnje oglišče mora biti isto prvemu
    
    m = int(sys.stdin.readline()) #število točk za preverit
    for j in range(m):
        toč = Točka(sys.stdin.readline())
        print(točka_v_poligonu(toč, poligon))
    n = int(sys.stdin.readline()) #število oglišč naslednjega poligona