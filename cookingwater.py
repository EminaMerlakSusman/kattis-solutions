n = int(input())
intervali = []

'''Ugotoviti je treba, ali se intervali sekajo, torej ali je Edward pri vsakem kuhanju vode gledal stran
ravno v isti sekundi.
To se lahko naredi tako, da si nekam zapišemo vse sekunde, v katerih je Edward gledal stran, na koncu pa
pogledamo, ali se ta sekunda pojavi točno n-krat.'''

for i in range(n):
    inter = list(map(int, input().split()))
    for st in range(inter[0], inter[1] + 1):
        intervali.append(st)

def preveri(intervali):
    for k in intervali:
        if intervali.count(k) == n:
            return False
    return True

print('edward is right' if preveri(intervali) else 'gunilla has a point')

        
    
    
    
