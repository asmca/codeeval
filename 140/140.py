import sys

# add a comment

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test1,test2=test.strip().split(';')
    s1=test1.split()
    c=[int(x) for x in test2.split()]

    s2=s1
    for i,n in enumerate(c):
        s2[n-1]=s1[i]
    
    print s2


    



test_cases.close()

