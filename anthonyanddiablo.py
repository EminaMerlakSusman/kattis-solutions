import math

a, n = map(float, input().split())

rad = n/(2*math.pi)
ploscina = math.pi*rad**2

if ploscina >= a:
    print('Diablo is happy!')
else:
    print('Need more materials!')