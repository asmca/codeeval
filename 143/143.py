import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    t1,t2=test.split(';')
    
    #s1 is str
    s1=" ".join(t1.split())
    list1=[0 for x in range(len(s1))]
    for i in range(len(s1)):
        if s1[i]==' ':
            list1[i]=1


    #n2 is list
    n2=t2.split()

    #if not n2:
    #    print "I cannot fix history"
    #    continue
    
    
    s3=s1
    ifmatch=1
    idxs1=0

    for i,item in enumerate(n2):
        if i>0:
            if s3.find(' ')==-1:
                ifmatch=0
                break
            idxs1=idxs1+s3.index(' ')+1
            s3=s3[s3.index(' ')+1:]

        idx=s3.find(item)
        if idx == -1:
            ifmatch=0
            break
        for j in range(idxs1+idx,idxs1+idx+len(item)):
            list1[j]=1
        s3=s3[idx+len(item):]
        idxs1=idxs1+idx+len(item)

    if ifmatch:
        for i in range(len(s1)):
            if list1[i]==1:
                list1[i]=s1[i]
            else:    
                list1[i]='_'
        print ''.join(list1)        
        continue

    
    print "I cannot fix history"




test_cases.close()

