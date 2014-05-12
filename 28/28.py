import sys


def ifmatching(s,t):
    for i in t:
        if not i:
            return True
        if s.find(i)==-1:
            return False
        s=s[ s.index(i)+len(i):]
    return True    
        




test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s1,s2=test.split(',')
    
    # to avoid scenario of \*
    # chaning to '#' for tmp
    s1=s1.strip().replace("*","#")
    s2=s2.strip().replace("\*","#")

    t2=s2.split('*')
    print  "true" if ifmatching(s1,t2) else "false"


test_cases.close()
