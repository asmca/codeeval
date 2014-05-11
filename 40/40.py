import sys

def isSDC(n):
    strn=str(n)
    for i in range(len(strn)):
        biti=int(strn[i])
        counti=strn.count(str(i))
        if biti != counti:
            return False
    return True    

test_case = open(sys.argv[1],'r')

for test in test_case:
    num=int(test)
    print 1 if isSDC(num) else 0

test_case.close()    


