import sys


def myreverse(a,m,n):
    a[m],a[n]=a[n],a[m]

#    if m>n:
#        m,n=n,m
#    if m==n:
#        return a
#    a[m],a[n]=a[n],a[m]
#    if n-m ==1:
#        return a
#    if n-m ==2:
#        return a
#    if n+1==len(a) or m ==0:
#        return myreverse(a,m+1,n-1)
#    a[m+1:n]=a[n-1:m:-1]
#    return a
#
    


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    myarr=test.split(':')[0].strip().split(' ')
    mycmd=test.split(':')[1].strip().split(',')

    for i in mycmd:
        i1=int(i.split('-')[0])
        i2=int(i.split('-')[1])
        myreverse(myarr,i1,i2)
        #print newarr

    print ' '.join(myarr)    
    
test_cases.close()

