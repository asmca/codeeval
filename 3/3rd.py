from itertools import count

def isPrime(n):
    if n<=1:
        return False
    for i in count(2):
        if i*i>n:
            return True
        if n%i==0:
            return False


def isPanlindrome(n):
    strn=str(n)
    if strn == strn[::-1]:
 #   if strn == ''.join(reversed(strn))
        return True


start=10000000

for n in count(start,-1):
    if isPrime(n) and isPanlindrome(n):
        print n
        break
    if n<=1:
        break
        



