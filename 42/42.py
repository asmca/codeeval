import sys

# func pall to print all possible combinations 
# in a list t
def pall(s):
    if len(s)==1:
        return list(s)
    t=[]
    for i in '+','-','':
        t1=pall(s[1:])
        for j in t1:
            t.append(s[0]+i+j)
    return t


# calculate the number of ugly#, 
# parameter is the list above, return from pall()
def calugly(t):
    num=0
    for i in t:
        #if i>1 and not i%2 or not i%3  or not i%5:
        if  not i%2 or not i%3  or not i%5 or not i%7:
            num=num+1
    return num


# here we hit a problem on eval
# for example:
#    eval('011')=9 not 11
# we need to avoid this problem
# eval(x.lstrip('0'))
#
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=test.strip()
    t=pall(s)
    t1=[eval(x.lstrip('0')) for x in t]
    print calugly(t1)
    
test_cases.close()
    




