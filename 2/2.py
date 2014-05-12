import sys

mylist=[]

test_cases = open(sys.argv[1], 'r')
nu=int(test_cases.readline())
for test in test_cases:
    mylist.append(test.strip())
test_cases.close()


print '\n'.join(sorted(mylist,cmp=lambda x,y:cmp(len(x),len(y)),reverse=True)[:nu])

