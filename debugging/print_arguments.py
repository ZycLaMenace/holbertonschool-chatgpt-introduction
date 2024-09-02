#!/usr/bin/python3
 # for i in range(1, len(sys.argv)):
  #  print(sys.argv[i])

import sys # more pythonique way 

for arg in sys.argv[1:]:
    print(arg)