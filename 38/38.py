import sys

def permutation(s,count):
    if count==1:
        return list(s)
    t=[]
    for i,n in enumerate(s):
        for j in permutation(s,count-1):
            t.append(n+j)
    return t


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    count,s=test.strip().split(',')

    #simplify the countings
    count=int(count)
    s=''.join(set(s))


    t=permutation(s,count)
    t.sort()
    print ','.join(t)

test_cases.close()

