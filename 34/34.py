import sys

test_case=open(sys.argv[1],'r')


for test in test_case:
    if not test.strip():
        continue

    mylist=[int(x) for x in test.split(';')[0].split(',')]
    sorted(mylist)
    mynum=int(test.split(';')[1])

    i=0
    j=len(mylist)-1
    pairs=[]
    

    while j>i:
        if mylist[i]+mylist[j]==mynum:
            pairs.append((mylist[i],mylist[j]))
            deltai=mylist[i+1]-mylist[i]
            deltaj=mylist[j]-mylist[j-1]
            if deltai<deltaj:
                i=i+1
            else:
                j=j-1
        elif mylist[i]+mylist[j]<mynum:
            i=i+1
        else:
            j=j-1

    print ';'.join(str(x[0])+','+str(x[1]) for x in pairs) if pairs else "NULL"

test_case.close()    




