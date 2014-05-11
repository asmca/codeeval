import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    print test.title(),
 

test_case.close()    


