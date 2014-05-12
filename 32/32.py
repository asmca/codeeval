import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    a=list(test.strip().split(',')[0])
    b=list(test.strip().split(',')[1])
    
    a.reverse()
    b.reverse()

    print 1 if a[:len(b)]==b else 0
    
test_cases.close()

