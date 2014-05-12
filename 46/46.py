import sys

def isPrime(n):
    if n<2 or n==4:
        return False
    if n ==2 or n==3 or n==5:
        return True
    for i in range(2,int(pow(n,.5)+1)):
        if not n%i:
            return False
    return True


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist=[x for x in range(2,int(test)) if isPrime(x)]        
    
    print ','.join(str(x) for x in mylist)

test_cases.close()



