
s = input()
uppers = 0
lowers = 0
nums = 0
white = 0
l = len(s)
for i in s:
    if i.isupper():
        uppers += 1
    elif i.islower():
        lowers += 1
    elif i == '_':
        white += 1
    else:
        nums += 1
print(white/l)
print(lowers/l)
print(uppers/l)
print(nums/l)