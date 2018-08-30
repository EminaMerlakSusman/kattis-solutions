import math
line = list(map(float, input().split()))
rezine = int(line[0])
polkrogi = int(line[1])
r = line[2]
koords = list(map(int, input().split()))

t1 = tuple(koords[:2])
t2 = tuple(koords[2:])

'''med dvema točkama sta dve poti:
-  po ulici navzdol gremo do nižje izmed obeh točk,
   nato pa po kanalu prepotujemo do druge točke.
-  potujemo samo po ulicah, torej od ene točke naravnost do 0,
   nato pa od 0 naravnost do druge točke.'''

#razdalja po prvem načinu:
def y_dist(y1, y2, r, polkrogi):
    return (abs(y2 - y1) / polkrogi)*r #delež radija, ki ga predstavlja razlika med y-onoma

def x_dist(tocka1, tocka2, st_rez, radij):
    x1 = tocka1[0]
    x2 = tocka2[0]
    y1 = tocka1[1]
    y2 = tocka2[1]
    return (abs(x1 - x2) / st_rez)*math.pi*radij #pi*radij je obseg polkroga

manjsi_r = min(t1[1], t2[1]) #pot je krajša, če gremo po krajšem kanalu (razlika med y-onoma je v vsakem primeru enaka)
razy = y_dist(t1[1], t2[1], r, polkrogi) 
razx = x_dist(t1, t2, rezine, (manjsi_r/polkrogi)*r)
raz1 = razx + razy

#razdalja po drugem načinu:
def radij_dist(tocka1, tocka2, polkrogi, radij):
    y1 = tocka1[1]
    y2 = tocka2[1]
    r1 = (y1/polkrogi)*radij #delež radija, 
    r2 = (y2/polkrogi)*radij #ki ga predstavljata y1 in y2
    return r1 + r2

raz2 = radij_dist(t1, t2, polkrogi, r)

print(min(raz1, raz2))



