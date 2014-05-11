import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    print test.lower(),


test_case.close()    


