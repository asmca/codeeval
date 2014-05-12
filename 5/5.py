import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist=test.strip().split(' ')
    for i in range(len(mylist)):
        if mylist[i] in mylist[:i]:
            print ' '.join(w for w in mylist[mylist.index(mylist[i]):i])
            break

test_cases.close()



