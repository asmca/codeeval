import sys
from itertools import count

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
   x,n=test.split(',')
   for i in count(2):
       if int(n)*i >= int(x):
           print int(n)*i
           break


test_cases.close()

