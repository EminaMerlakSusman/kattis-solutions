import sys

'''Izračuna PDC(n, v): število permutacij P reda N,
katere imajo v descentov.'''

tabela_descentov = [[None for i in range(101)] for j in range(101)]
for j in range(1, 101):
    tabela_descentov[j][j - 1] = 1

'''Da iz permutacije 1...(n - 1) dobimo permutacijo 1...n, lahko vstavimo n v katerokoli od n mest v prvi permutaciji (na začetek, konec, ali pa med dva sosednja elementa permutacije). Če n vstavimo med dva elementa, ki tvorita descent, ni ustvarjen noben nov descent. Če n vstavimo na konec, prav tako ni ustvarjen noben nov descent. Sicer pa je ustvarjen nov descent. 
Torej lahko iz permutacije reda n-1 z d descenti dobimo
•	d + 1 permutacij reda n z d descenti
•	n -d – 1 permutacij reda n z d + 1 descenti

Da dobimo permutacijo reda n z d descenti, lahko:
•	vzamemo permutacijo reda n – 1 z d descenti in vstavimo n na konec ali pa med dva sosednja elementa, ki že tvorita descent (to lahko storimo na d + 1 načinov), ali
•	vzamemo permutacijo reda n – 1 z d – 1 descenti in vstavimo n na začetek ali med dva sosednja elementa, ki ne tvorita descenta (to lahko storimo na (n - 1) – (d - 1) načinov, oz. (n – d) načinov), torej:
PDC(n ,d) = PDC(n – 1, d) * (d + 1) + PDC(n - 1, d - 1) * (n – d)'''

def PDC(n, v):
    '''Uporabi rekurzivno formulo za izračun PDC(n, v)'''
    if v == 0 or v == n - 1:
        return 1
    if tabela_descentov[n][v] != None: #če smo za ta n in v že izračunali vrednost,
        #vrnemo tisto kar smo takrat izračunali
        return tabela_descentov[n][v]
    tabela_descentov[n][v] = ((v + 1) * PDC(n - 1, v) + (n - v) * PDC(n - 1, v - 1)) %  1001113
    return tabela_descentov[n][v]
    
testi = sys.stdin.readline()

for _ in range(int(testi)):
    vrs = sys.stdin.readline().split()
    red = int(vrs[1])
    št = int(vrs[2])
    print(vrs[0] + " " +str(PDC(red, št)))
