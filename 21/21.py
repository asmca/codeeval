import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    sum=0
    for i in range(len(test)-1):
        sum+=int(test[i])
    print sum


test_case.close()    


