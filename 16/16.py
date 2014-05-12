import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num=int(test)
    count=0
    while num:
        count=count+1 if num&1 else count
        num=num>>1
    print count

test_cases.close()

