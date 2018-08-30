'''Na podlagi podanega zaporedja ukazov zpiše število bitk, ki jih je naš heroj dobil.''' 
n = int(input()) #število bitk
zgubil = 0
for i in range(n):
    zap = input()
    for i in range(len(zap) - 1):
        if zap[i] == 'C':    #naš heroj je izgubil vsako bitko,
            if zap[i + 1] == 'D': #kjer ukazu C sledi ukaz D.
                zgubil += 1
print(n - zgubil)