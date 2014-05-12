import sys,math


myrev=[0,1,2]
mylevel=[pow(2,x) for x in range(31,-1,-1)]

def findNth(n):
    if n==0:
        return 0
    count=0
    while n>=1:
        for i in mylevel:
            if n>=i:
                n=n-i
                count=count+1
#    while n>1:
#        base=int(math.log(n,2)) #base<32
#        n=n-pow(2,base)
#        count=count+1
    return myrev[(count)%3]
    

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n=int(test)
    
    print findNth(n)
test_cases.close()
