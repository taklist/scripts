import os

pathfile = open("journalpath")
path = ''

for line in pathfile:
    if line.startswith('journalpath='):
        path = line.split('=')[1]

if path is '':
    print 'Error: Missing journalpath file/line\n'
    sys.exit()

files = os.listdir(path)

num_days = 0
total_hours = 0

for i in files:
    try:
        fil = open(path + i, 'r')
        total_hours += float(fil.readline())
        if '_1' in i:
            num_days += 1
    except IOError:
        print "Error reading from file"
    except ValueError:
        print "Missing value in: ", fil
        
print '  Total files: ', num_days
print '  Total hours: ', total_hours
print 'Average hours: ', total_hours/num_days
