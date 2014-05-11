import sys

test_case = open(sys.argv[1],'r')
for test in test_case:
    s1=test.strip().split(',')[0]
    s2=test.strip().split(',')[1]

    s1=s1+s1

    print False if s1.find(s2)==-1 else True

test_case.close()    
