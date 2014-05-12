import sys

def isPrime(n):
    if n<2:
        return False
    if n == 2:
        return True
    for i in range(2,int(pow(n,.5)+1.1)):
        if not n%i:
            return False
    return True


test_case = open(sys.argv[1],'r')

for test in test_case:
    a=int(test.split(',')[0])
    b=int(test.split(',')[1])

    sum=0
    for i in range(a,b+1):
        sum=sum+1 if isPrime(i) else sum
    print sum

test_case.close()


