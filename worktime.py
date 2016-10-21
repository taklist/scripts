import os
path = '../work_journal/'
files = os.listdir(path)

num_days = 0
total_hours = 0

for i in files:
    try:
        fil = open(path + i, 'r')
        total_hours += int(fil.readline())
        if '_1' in i:
            num_days += 1
    except IOError:
        print "Error reading from file"
    except ValueError:
        print "Missing value in: ", fil
        
print '  Total files: ', num_days
print '  Total hours: ', total_hours
print 'Average hours: ', total_hours/num_days
