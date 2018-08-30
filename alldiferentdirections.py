import math

def razdalja_na_kvadrat(a, b):
    '''Kvadrat razdalje med točkama a in b.'''
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    return (x1 - x2)**2 + (y1 - y2)**2

def naslednja(tocka, razdalja, kot):
    '''Izračuna točko, v katero prideš, ko imaš podano
    začetno točko, razdaljo med točkama, ter kot, za katerega se obrneš.'''
    x2 = float(tocka[0]) + float(razdalja*math.cos(math.radians(kot)))
    y2 = float(tocka[1]) + float(razdalja*math.sin(math.radians(kot)))
    return x2, y2

n = int(input())
while n != 0:
    lokacije = []
    for i in range(n):
        nav = input().split()
        lok = (float(nav[0]), float(nav[1])) #to je tvoja začetna lokacija
        kot = float(nav[3])
        razdalja = 0
        for k in range(4, len(nav)): #gledamo od prvega 'walk' naprej
            if nav[k] == 'turn':
                kot += float(nav[k + 1])
            elif nav[k] == 'walk':
                razdalja = float(nav[k + 1])
                lok = naslednja(lok, razdalja, kot)
        lokacije.append(lok)
        x_avg, y_avg = (0, 0) #izračun povprečne razdalje
        for tuple in lokacije:
            x_avg += tuple[0]
            y_avg += tuple[1]
        x_avg /= len(lokacije)
        y_avg /= len(lokacije)
        d = 0
        for tuple in lokacije: #iskanje največjega odstopanja od povprečja
            d1 = razdalja_na_kvadrat(tuple, (x_avg, y_avg))
            if d1 > d:
                d = d1
    print("{:.2f} {:.2f} {:.2f}".format(x_avg, y_avg, math.sqrt(d)))
    n = int(input())   
