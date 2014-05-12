from itertools import count

def isPrime(n):
    if n<=1:
        return False
    for i in count(2):
        if i*i>n:
            return True
        if n%i==0:
            return False

nu_prime=0
current=2
summary=0


for n in count(current):
    if isPrime(n):
        summary+=n
        nu_prime+=1
    if nu_prime >= 1000:
        break

print summary


