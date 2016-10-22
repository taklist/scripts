import os
import sys
import threading
import time

minutes = int(sys.argv[1])



# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    c = '-closeLabel No'
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, c])))


for i in range(int(sys.argv[1])):
    print 'Minutes remaining: ', int(sys.argv[1])-i
    time.sleep(60)
    
# Calling the function
notify(title    = 'Work Timer',
       subtitle = sys.argv[1],
       message  = 'You are finished!')
