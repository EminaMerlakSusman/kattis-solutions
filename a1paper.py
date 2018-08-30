import math
n = int(input())
l = str(input()).split()
listi = list(map(lambda x: int(x), l))

sum = 0 #dolžina selotejpa, ki ga rabimo
manjka = 1 
dolzina_stranice = math.pow(2, -0.75)
for i in range(len(listi)):
    sum += dolzina_stranice*manjka 
    manjka = manjka*2 - listi[i] #vsakega formata rabimo 2* več kot prejšnjega formata, minus
    #število, koliko jih že imamo
    dolzina_stranice = dolzina_stranice/math.sqrt(2)
print('impossible' if manjka > 0 else sum) #če nam na koncu še manjka listov, je stvar nemogoča

