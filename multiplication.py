'''Nariše tabelo množenja.'''

operanda = input().split()
a = int(operanda[0])
b = int(operanda[1])

while (a, b) != (0, 0):
    produkt = a*b
    #zgoraj na začetek damo dva minusa in plus na vsako stran, vmes pa nad vsako števko
    #po 3 minuse, ter minus vmes med števkami
    print('+--' + (len(str(a)) - 1)*'-' + len(str(a))*3*'-' + '--+')
    #vrstica s prvim operandom
    print('|  ', end = ' ')
    for znak in str(a):
        print(znak + ' '*3, end = '')
    print('|')
    #vmesna vrstica
    print('| +', end = '')
    for znak in str(a):
        print('---+', end = '')
    print(' |')
    #računanje rezultatov
    zmnožki = []
    for znak in str(b):
        vrstica = []
        for stevka in str(a):
            vrstica.append(int(int(stevka)*int(znak)))
        zmnožki.append(vrstica)
    dolz =len(str(b))+len(str(a))
    strProdukt = str(produkt).zfill(dolz) #vodilne ničle
    #sestavljanje vrstic
    for i in range(len(zmnožki)):
        if i == 0 or strProdukt[i - 1] == '0':
            print('| |', end = '')
        else:
            print('|/|', end = '')
        vrsta = zmnožki[i]
        for st in vrsta:
            print('{} /|'.format(st//10), end = '') #to je vrsica z deseticami
        print(' |')
        #vmesna vrstica
        print('| |', end = '')
        for _ in range(len(str(a))):
            print(' / |', end = '')
        print('{}|'.format(str(b)[i]))
        #druga vrstica (z enicami)
        if strProdukt[i]  != '0': #vodilnih ničel ne smemo printat
            print('|{}|'.format(strProdukt[i]), end = '') #števke produkta ob strani
        else:
            print('| |', end = '')
        for st in vrsta:
            print('/ {}|'.format(st % 10), end = '')
        print(' |')
        #druga vmesna vrsta
        print('| +', end = '')
        for znak in str(a):
            print('---+', end = '')
        print(' |')
    #predzadnja vrstica s preostalim produktom
    if len(str(produkt)) == 1: #v tem primeru ne pišemo slasha spredaj
        print('|  ', end = '')
    else:
        print('|/ ', end = '')
    strOst = strProdukt[len(str(b)):]
    for k in range(len(strOst) - 1):
        print('{} / '.format(strOst[k]), end = '')
    print(strOst[-1] + '    |')
    print('+--' + (len(str(a)) - 1)*'-' + len(str(a))*3*'-' + '--+')
    operanda = input().split()
    a = int(operanda[0])
    b = int(operanda[1])
