import time
import sys

for i in range(10):
    print i,
    if i == 5:
        print "Flushing buffer"
        sys.stdout.flush()
    time.sleep(1)

for i in range(10):
    print i,
    if i == 5:
        print "Flushing buffer"
        sys.stdout.flush()
