import sys
from itertools import count

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print 0 if int(test)&1 else 1
    


test_cases.close()

