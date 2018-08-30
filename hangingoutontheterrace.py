'''Ugotovi, koliko skupin ljudi ni smelo priti na teraso.'''

s = list(map(int, input().split()))
limita = s[0]
dogodki = s[1]
na_terasi = 0
zavrnjenih = 0
for i in range(dogodki):
    niz = input().split()
    dogodek = niz[0]
    stevilo_ljudi = int(niz[1])
    if dogodek == 'enter':
        if na_terasi + stevilo_ljudi > limita: #če hoče prevelika skupina priti na teraso
            zavrnjenih += 1 #jih zavrnjemo
        else:
            na_terasi += stevilo_ljudi #se poveča število ljudi na terasi
    elif dogodek == 'leave':
        na_terasi -= stevilo_ljudi #se pomanjša število ljudi
print(zavrnjenih)