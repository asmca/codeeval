import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num=int(test)
    if num==0:
        print 0
        continue
    blist=[]
    while num:
        blist.append('1') if num&1 else blist.append('0')
        num=num>>1
    blist.reverse()
    print ''.join(blist)

test_cases.close()

