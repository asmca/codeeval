import sys

test_case=open(sys.argv[1],'r')
for test in test_case:
    num=int(test, 16)
    print num

test_case.close()    
