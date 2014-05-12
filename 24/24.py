import sys

test_case=open(sys.argv[1],'r')

sum=0

for test in test_case:
    sum+=int(test)

print sum

test_case.close()
