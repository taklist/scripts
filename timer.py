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

time.sleep(minutes*60)
    
# Calling the function
notify(title    = 'A Real Notification',
       subtitle = 'with python',
       message  = 'Hello, this is me, notifying you!')

