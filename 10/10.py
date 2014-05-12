import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    myin=test.strip().split(' ')
    mystr=myin[:-1]
    myindex=int(myin[-1])
    if myindex>len(mystr):
        continue
    newindex=len(mystr)-myindex
    print mystr[newindex]

test_cases.close()



