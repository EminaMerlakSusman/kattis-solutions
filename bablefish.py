import sys
line = sys.stdin.readline()
dict = {}
while line != '\n':
    line = line.split(' ')
    dict[line[1]]=line[0]
    line = sys.stdin.readline()

text = sys.stdin.readline()
while text != '':
    try:
        print(dict[text])
    except KeyError:
        print('eh')
    text = sys.stdin.readline()
    