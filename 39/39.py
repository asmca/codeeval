import sys

def sumOfSquare(n):
    strn=str(n)
    sum=0
    for i in range(len(strn)):
       biti=int(strn[i])
       sum+=int(biti*biti)
    return sum

def isHappy(n):
    isArray=[]
    while 1:
        if n==1:
            return True
        else:
            if n in isArray:
                return False
            isArray.append(n)
            n=sumOfSquare(n)


test_case = open(sys.argv[1],'r')

for test in test_case:
    num=int(test)
    print 1 if isHappy(num) else 0

test_case.close()    


