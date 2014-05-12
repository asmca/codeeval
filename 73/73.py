import sys

LIST=[str(x) for x in range(1,27)]

def DecodeNumber(a,b='1'):
    if b not in LIST:
        return 0
    if not a:
        return 1
    if len(a)==1: # and a[0] in LIST, it's ok to ignore
        return 1
    return DecodeNumber(a[1:],a[0])+DecodeNumber(a[2:],a[:2])


test_case = open(sys.argv[1],'r')

for test in test_case:
    case=test.strip()
    
    print DecodeNumber(case)

test_case.close()    
