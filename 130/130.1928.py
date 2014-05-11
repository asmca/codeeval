import sys,re


# m is char, n is str
# m is 0 or 1
# n is sequence that only contains A and B
# avoid using regex here.
#def ifmatching(m,n):
#    if not n or not m:
#        return False
#    if m=='0':
#        if 'B' not in n:
#            return True
#        return False
#    if m=='1':
#        if 'B' not in n or 'A' not in n:
#            return True
#        return False
#    return False


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

    # init mtx[0], 1st row, check s1[0] if matching s2[0-?]
    for j in range(y-x+1):
        if ifmatching(s1[0],s2[:j+1]):
            mtx[0][j]=1
    
    for i in range(1,x):
        for j in range(i,y-x+1+i):
            # set mtx[i][j]
            for k in range(i-1,j):
                if mtx[i-1][k]:
                    if ifmatching(s1[i],s2[k+1:j+1]):
                        mtx[i][j]=1
                        break

    print "Yes" if mtx[x-1][y-1] else "No"

test_cases.close()
