import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    s,a=test.split()
    s1= [ int(x) for x in s.strip('()').split(',')     ] #x
    a1= [ int(x) for x in a.strip('()').split(',')     ] #y
    

    #rate = s1[-1]/a[-1] or reverse...

    sum=0
    for x in range(1,len(s1)):   #x,y
        for y in range(1, len(a1)):
            if a1[-1]*s1[x] >s1[-1]* a1[y-1] and a1[-1]*s1[x-1] <s1[-1]*a1[y]:
                sum=sum+1

    print sum



test_case.close()    

