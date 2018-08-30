st_delov, st_dni = tuple(map(int, input().split()))

sez_delov = []
st_zamenjanih = 0
dan_zamenjave = None
for i in range(st_dni):
    ta_del = input()
    if ta_del not in sez_delov:
        st_zamenjanih += 1
        sez_delov.append(ta_del)
    if st_zamenjanih == st_delov and dan_zamenjave == None:
        dan_zamenjave = i + 1
if dan_zamenjave == None:
    print('paradox avoided')
else:
    print(dan_zamenjave)