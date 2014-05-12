import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist=list(test.strip())
    for i in mylist:
        if i not in mylist[mylist.index(i)+1:]:
            print i 
            break
test_cases.close()

