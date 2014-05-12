import sys

test_case=open(sys.argv[1],'r')

#A change here for changes on Notation,
#Im just ignoring N input for saving time
#code should be updated for N, X fetch
test_case.readline()

for test in test_case:
    nu=int(test)

    mylist=[pow(x,2) for x in range(int(pow(nu,.5)+1))]
    
    DEGREE=0

    i=0
    j=len(mylist)-1
    
    while j>=i:
        if mylist[i]+mylist[j]==nu:
            DEGREE=DEGREE+1
        if mylist[i]+mylist[j]<=nu:
            i=i+1
        else:
            j=j-1

    print DEGREE


test_case.close()    



