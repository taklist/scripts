import time
import sys
import os.path

try:
    hours = float(input('Enter hours of work: '))
    if hours > 10:
        if raw_input('Really? y/n: ') != 'y':
            sys.exit()
            
except NameError:
    print 'Invalid input'
    sys.exit()
except SyntaxError:
    print 'Invalid input'
    sys.exit()


contents = []
while True:
    try:
        line = raw_input("")
    except EOFError:
        break
    contents.append(line)

desc = ''
for line in contents:
    desc += line
    desc += '\n'

    
i=1
while True:
    if os.path.exists(time.strftime('../work_journal/%d%m%y_') + str(i)):
        i+=1
    else:
        break
    

f = open(time.strftime('../work_journal/%d%m%y_' + str(i)), 'w+')
f.write(str(hours) + '\n\n' + desc + '\n')
f.close()
