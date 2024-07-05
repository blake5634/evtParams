import sys

fname = sys.argv[1]

f = open(fname, 'r')

tlist = ['Pintercept', 'Fintercept', 'Vintercept']
output = []
for line in f:
    save = True
    for target in tlist:
        if target in line:
            save = False
    if save:
        output.append(line)

f.close()
f=open(fname, 'w')
for line in output:
    print(line, file=f,end='')
f.close()
