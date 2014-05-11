import sys

def Line_Yanghui(n,i):
    if i==0 or i==n:
        return 1
    else:
        return Line_Yanghui(n-1,i-1)+Line_Yanghui(n-1,i)

test_case = open(sys.argv[1],'r')

for test in test_case:
    a=int(test)

    for x in range(a):
        for y in range(x+1):
            print Line_Yanghui(x,y),
    
    print

test_case.close()    


