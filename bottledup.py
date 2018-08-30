'''Na podlagi podanega volumna olja izračuna, če je možno, da bi olje razporedili v cilindre
volumnov v1 in v2. Če je to možno, vrne število potrebnih cilindrov v1 in v2.'''

string = list(map(int, input().split()))
volPošiljka = string[0]
volVečji = string[1]
volManjši = string[2]

#vsaka flaša je napolnjena do vrha
#ans = x*9 + y*7
#od s odštevamo večkratnike v2, dokler ne pridemo do
#večkratnika v1. Če ne pridemo do večkratnika v1,
#prinatamo 'impossible'.
#če pa ga najdemo, printamo večkratnik/v2 in i

najv = volPošiljka//volManjši
najden = False
for i in range(najv + 1):
    razlika = volPošiljka - i*volManjši
    if razlika % volVečji == 0:
        najden = True
        break
if not najden:
    print('Impossible')
else:
    print(int(razlika /volVečji), i)