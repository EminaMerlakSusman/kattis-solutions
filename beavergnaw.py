import math
line = tuple(map(int, input().split()))

D = line[0]
V = line[1]

while (D, V) != (0, 0):
    volumen_vel = (math.pi*D**3)/4
    procent = 1 - (V/volumen_vel)
    volumen_manj = procent*volumen_vel
    print((D**3 - 6*V/math.pi)**(1/3))
    line = tuple(map(int, input().split()))
    D = line[0]
    V = line[1]
