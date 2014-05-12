import sys

#here Im using string instead of int for caculations

def RevAdd(n):
    return str(int(n)+int(n[::-1]))

def isPalindrome(n):
    return n==n[::-1]



test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    out=test.strip()
    count=0

    while 1:
        out=RevAdd(out)
        count=count+1
        if isPalindrome(out):
            print count,out
            break


test_cases.close()



