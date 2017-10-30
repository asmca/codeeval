import sys

def mymax(s1,s2):
    if not s1:
        return 0,None
    if not s2:
        return 0,None
    c1=s1[0]
    if len(s1)==1:
        if s2.find(c1)==-1:
            return 0,None
        else:
            return 1, [c1]
    if s2.find(c1)==-1:
        return mymax(s1[1:],s2)
    maxin=mymax(s1[1:],s2[s2.index(c1)+1:])
    maxnotin=mymax(s1[1:], s2)
    if maxin[0]+1>=maxnotin[0]:
        mylist=[c1]
        if maxin[1]:
            mylist.extend(maxin[1])
        return maxin[0]+1,mylist
    else:
        return maxnotin


test_case = open(sys.argv[1],'r')

for test in test_case:
    if not test.strip():
        continue

    ss1,ss2=test.strip().split(';')

    print ''.join(mymax(ss1,ss2)[1])

test_case.close()

