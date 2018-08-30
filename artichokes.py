import math

'''Izračuna največji padec cene delnice v določenem časovnem obdobju.
Spremenljivke p, a, b, c, d, in n so tako neumno poimenovane zato, ker so take tudi v
navodilih naloge, in ni opisano, kaj posamezna spremenljivka pomeni.'''

def cena(k, p, a, b, c, d):
    '''Funkcija, ki izračuna ceno(k) na podlagi konstant p, a, b, c, in d
    po formuli, ki je v navodilih.'''
    return p*(math.sin(a*k + b) + math.cos(c*k + d) + 2)

cene = []

p, a, b, c, d, n = tuple(map(int, input().split()))

#to je prepočasno, zato je zakomentirano:

##for k in range(1, n + 1):
##    cene.append(cena(k, p, a, b, c, d))

#največja izguba v določenem časovnem obdobju
naj_raz = 0
naj_vrednost = cena(1, p, a, b, c, d)
for i in range(2, n + 1):
    naslednja = cena(i, p, a, b, c, d) #cena(k)
    if naslednja >= naj_vrednost:
        naj_vrednost = naslednja
    elif naj_vrednost - naslednja > naj_raz: #če je razlika večja kot prej
        naj_raz = naj_vrednost - naslednja  #nastavimo to razliko za največjo
print(float(naj_raz))