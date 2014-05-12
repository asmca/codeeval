import sys,re

mylist={'0':"A+",
        '1':"(B+|A+)"
        }

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s1,s2=test.strip().split(' ')
    ss1=''.join([mylist[x] for x in s1 ])

    re1=re.compile(ss1)
    print ss1
    print "Yes" if re1.match(s2) else "No"


test_cases.close()
