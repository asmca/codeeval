import sys

from itertools import count


def fib(n):
    if n>2:
        a,b=1,1
        for i in count(3):
            a,b=a+b,a
            if i>=n:
                return a
    elif n==2:
        return 1
    elif n==1:
        return 1
    else:
        return 0


test_case = open(sys.argv[1],'r')

for test in test_case:
    num=int(test)
    print fib(num)

    
        
    


test_case.close()    


