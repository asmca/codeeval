import sys

def numi(t):
    # when t is empty, return 0
    if not t:
        return 0
    if len(t)==1:
        return 0 if t[0] else 1
    # when length >1
    if t[0]: # when 1st value is True
        if True not in t[1:]:
            return numi(t[1:])
        i=t[1:].index(True)+1 # Next / 2nd True pos
        # return 1+      numi(t[i+1:])      +numi(t[1:])
        # above is not correct, on block t[i+1:], we dont need total
        # we need begin ^ with  i+1, 
        #   :::  numi(t[i+1:]) -numi(t[i+2:]) 
        # return 1+      numi(t[i+1:])      +numi(t[1:])
        return 1+      numi(t[i+1:]) -numi(t[i+2:])     +numi(t[1:])
    #else when 1st value if False
    # Also we need to update here, only need ^ with t[1:]
    return 1+2*numi(t[1:])-numi(t[2:]) 



test_case = open(sys.argv[1],'r')

for test in test_case:
    s1,s2=test.split()
    n1=int(s1)
    n2=int(s2)
    
    # a list of scope who is palindromic , set TRUE
    t=[ str(x)[::-1]==str(x) for x in range(n1,n2+1)]


    print numi(t)
test_case.close()
