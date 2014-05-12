import sys


def mycount(s,n,d=4):
    if d<0:
        return 0
    if len(s)<d:
        return 0
    if len(s)==d:
        return 1 if sum(s)==n else 0
    return mycount(s[1:],n,d)+mycount(s[1:],n-s[0],d-1)
    

test_case = open(sys.argv[1],'r')

for test in test_case:
    mylist=[int(x) for x in test.strip().split(',') ]

    print mycount(mylist,0)
test_case.close()    
