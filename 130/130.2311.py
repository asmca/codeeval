import sys

def ifmatching(m,n):
    if not n or not m:
        return False
    if 'B' not in n:
        return True
    if 'A' in n:
        return False
    if m=='1':
        return True
    return False



test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s1,s2=test.strip().split(' ')
    x,y=len(s1),len(s2) #x is length of 1st argument, y is 2nd.

    if x>y or x<1 or y<1:
        print "No"
        continue

    # mtx initilized as 0 all.
    mtx=[[0 for col in range(y)] for row in range(x)]

    # len of s1=1, just a simple check.
    if x==1:
        print "Yes" if ifmatching(s1,s2) else "No"
        continue
    
    # init mtx[0], 1st row, check s1[0] if matching s2[0-?]
    # i=0
    for j in range(y-x+1):
        if ifmatching(s1[0],s2[:j+1]):
            mtx[0][j]=1

    
    for i in range(x-2):
        for j in range(i,y-x+1+i):
            if mtx[i][j]==1:
                for k in range(j+1,y-x+2+i):
                    if not mtx[i+1][k]:
                        if not ifmatching(s1[i+1],s2[j+1:k+1]):
                            break
                        mtx[i+1][k]=1


    # i=x-2 , j in range(y-1)
    i=x-2
    for j in range(y-1):
        if mtx[i][j]:
            if ifmatching(s1[x-1],s2[j+1:]):
                mtx[x-1][y-1]=1
                break


    print "Yes" if mtx[x-1][y-1] else "No"

test_cases.close()
