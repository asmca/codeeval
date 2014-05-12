import sys

def permutation(s):
    if len(s)==1:
        return list(s)
    t=[]
    for i,n in enumerate(s):
        for j in permutation(s[:i]+s[i+1:]):
            t.append(n+j)
    return t


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    t=permutation(test.strip())
    t.sort()
    print ','.join(t)

test_cases.close()

