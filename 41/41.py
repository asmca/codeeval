import sys

#ignore the length, and try dictionary

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mydict={}
    mylist=test.strip().split(';')[1].split(',')
    for i in mylist:
        mydict[i]=1 if i not in mydict else mydict[i]+1

    print ''.join(i for i in mydict if mydict[i]==2)

test_cases.close()





