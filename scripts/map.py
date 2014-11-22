#!/usr/bin/env python

import sys
import socket

hostname = socket.gethostname()

for line in sys.stdin:
    line = line.decode('string-escape').strip()

    words = line.split()

    for word in words:
        print "{0}-{1}\t{2}".format(hostname,word,1)
