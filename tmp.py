import sys
import glob
import et_lib as et

files = et.get_param_files()
for fn in files:
    print(fn)

x = input('OK??  ...<CR>...')

tlist = ['ET_diam']
print('Removing: ', tlist)

x = input('OK??  ...<CR>...')

for fn in files:
    f = open(fn,'r')

    output = []
    for line in f:
        save = True
        for target in tlist:
            if target in line:
                save = False
        if save:
            output.append(line)

    f.close()
    f=open(fn, 'w')
    for line in output:
        print(line, file=f,end='')
    f.close()


