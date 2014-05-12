import sys
from itertools import count

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    sn,sp1,sp2=test.split(',')
    n,p1,p2=int(sn),int(sp1),int(sp2)

    b1=(n&(1<<(p1-1)))>>(p1-1)


    b2=(n&(1<<(p2-1)))>>(p2-1)
    if (b1 == b2):
        print true
    else:
        print false
    


test_cases.close()

