import sys

comm = sys.stdin.readline().split()
commands = dict()

while comm != []:
    if comm[0] == 'def':
        commands[comm[1]] = int(comm[2])
    elif comm[0] == 'calc':
        calculation = ' '.join(comm[1:])
        try:
            result = commands[comm[1]]
            for i in range(1, len(comm[1:])):
                string = comm[i]
                if string == '+':
                    result += int(commands[comm[i + 1]])
                elif string == '-':
                    result -= int(commands[comm[i + 1]])
            #print(result)
            if result not in commands.values():
                result = 'unknown'
            else:
                for key, val in commands.items():
                    if val == result:
                        result = key
        except KeyError:
            result = 'unknown'
        print(calculation + ' {}'.format(result))
    elif comm[0] == 'clear':
        commands = dict()
    comm = sys.stdin.readline().split()