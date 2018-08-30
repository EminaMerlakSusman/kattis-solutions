dict = {0:'1', 1:'1', 2:'2', 3:'2', 4:'2', 5:'8'}
i = input().split()
for j in range(6):
    print(int(dict[j]) - int(i[j]), end = ' ')
    