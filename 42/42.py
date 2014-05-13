import sys,re

# func pall to print all possible combinations 
# in a list t
def pall(s):
    if not s:
        return []
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
    if not t:
        return 1
    num=0
    for i in t:
        #if i>1 and not i%2 or not i%3  or not i%5:
        if  not i%2 or not i%3  or not i%5 or not i%7:
            num=num+1
    return num


# following RE will compile and try to replace +/-0+ to +/-
p=re.compile('([+-])0+(?=\d)',re.VERBOSE)
# sample:
#         s='56-9+9+096-0234+0009-9934-400-009'
#     >>> p.sub(r'\1',s)
#         '56-9+9+96-234+9-9934-400-9'
#



# here we hit a problem on eval
# for example:
#    eval('011')=9 not 11
# we need to avoid this problem
# eval(x.lstrip('0'))
#
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # following lstrip('0') avoid invalid oct warning on beginning.
    #s=test.strip().lstrip('0')
    # update...
    # to reduce the complexity, we lstrip all left '0', cal the number *3
    #
    s=test.strip()
    s0=s.lstrip('0')
    #  if the string only having '0' sequence, calculate directly here.
    #  and return pow(3, num_0 -1)
    if not s0:
        # following 2 lines can be in 1 line
        print pow(3,len(s)-1)
        continue
    
    num_0=s.find(s0)
    s=s0
    


    t=pall(s)
    # for list t, it may contains item like '56-9+9+09+6'
    # we should change 09 -> 9 avoid invalid oct warning mesg.
    # processing t...
    # compile 2 RE before this for loop
    for i,n in enumerate(t):
        # this step we dont have to consider the '0' on left, we already lstrip on the beginning.
        if n.find('-0')>0 or n.find('+0')>0:
            n=p.sub(r'\1',n)
            t[i]=n

    

    t1=[eval(x.lstrip('0')) for x in t]
    print calugly(t1) * pow(3,num_0)
    
test_cases.close()
    




