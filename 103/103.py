import sys,json


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    myset=sorted(test.strip().split(' '))
    mydict={}
    for i in myset:
        if i not in mydict:
            mydict[i]=1
            continue
        mydict[i]+=1
    
    myset2=[x for x in mydict if  mydict[x] == 1]
    if not myset2:
        print 0
        continue
    print test.strip().split(' ').index(sorted(myset2)[0])+1

test_cases.close()

