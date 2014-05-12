import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test1,test2=test.strip().split(';')
    s1=test1.split()

    #by default last value is not list here.
    # append last value to list c
    c=[int(x) for x in test2.split()]
    for i in range(1,len(s1)+1):
        if i not in c:
            c.append(i)

    s2=s1[:]
    for i,n in enumerate(c):
        s2[n-1]=s1[i]
    
    print ' '.join(s2)

test_cases.close()

