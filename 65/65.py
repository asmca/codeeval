import sys 

L=['ABCE','SFCS','ADEE']


def findPathFromPoint(n,i,j,s,used=[]):
    if not s:
        return False
    if (i,j) in used:
        return False
    #print n,i,j
    if n[i][j]!=s[0]:
        return False
    if len(s)==1:
        return True

    used.append((i,j))

    #print "used",used
    result_up=findPathFromPoint(n,i-1,j,s[1:],used) if i>0 else False
    result_down=findPathFromPoint(n,i+1,j,s[1:],used) if i<2 else False
    result_left=findPathFromPoint(n,i,j-1,s[1:],used) if j>0 else False
    result_right=findPathFromPoint(n,i,j+1,s[1:],used) if j<3 else False

    return result_up or result_down or  result_left or result_right



def findPath(n,s):
    if not s:
        return False
    solution=False
    for i in range(3):
        for j in range(4):
            #print "solution",solution
            solution=solution or findPathFromPoint(n,i,j,s,[])
    return solution


test_case = open(sys.argv[1],'r')

for test in test_case:
    if not test.strip():
        continue
    line=test.strip()

    print findPath(L,line)
    



test_case.close()

