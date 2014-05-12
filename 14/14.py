import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    fromlist=list(test.split(',')[0])
    deletelist=list(test.split(',')[1].strip())
    for i in deletelist:
        while 1:
            if i not in fromlist:
                break
            fromlist.remove(i)
    print ''.join(fromlist)

test_cases.close()

