import sys

test_case = open(sys.argv[1],'r')

coinlist=[5,3,1]


for test in test_case:
    newlist=[]
    total=int(test)
    while total:
        for i in coinlist:
            if total>=i:
                newlist.append(i)
                total=total-i
                break
    print len(newlist    )


test_case.close()    
