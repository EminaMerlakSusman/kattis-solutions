premiki = [(0, 1), (1, 0), (0, -1),(-1, 0)]

board = []
for i in range(8):
    board.append(list(input()))
board[7][0] = '.'
navodila = input()
#print("Diamond!" if zelva_potuje(board, navodila) else "Bug!")

lokacija = (7, 0)
smer = 0
for znak in navodila:
    if znak == 'R':
        smer = (smer + 1) % 4
    elif znak == 'L':
        smer = (smer - 1) % 4
    elif znak == 'X':
        laser_koord = (lokacija[0] + premiki[smer][0], lokacija[1] + premiki[smer][1])
        if not 0 <= laser_koord[0] < 8 and 0 <= laser_koord[1] < 8:
            break
        if board[laser_koord[0]][laser_koord[1]] != 'I':
            break
        board[laser_koord[0]][laser_koord[1]] = '.'
    elif znak == 'F':
        nasl = (lokacija[0] + premiki[smer][0], lokacija[1] + premiki[smer][1])
        if not 0 <= nasl[0] < 8 and 0 <= nasl[1] < 8:
            break
        if board[nasl[0]][nasl[1]] not in '.D':
            break
        lokacija = nasl
    else:
        break
print('Diamond!' if board[lokacija[0]][lokacija[1]] == 'D' else 'Bug!')