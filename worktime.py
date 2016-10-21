import os
path = '../work_journal/'
files = os.listdir(path)

num_files = len(files)
total_hours = 0

for i in files:
    try:
        fil = open(path + i, 'r')
        total_hours += int(fil.readline())
    except IOError:
        print "Error reading from file"
    except ValueError:
        print "Missing value in: ", fil
        
print '  Total files: ', num_files
print '  Total hours: ', total_hours
print 'Average hours: ', total_hours/num_files

#TODO: calculate total_hours/days
