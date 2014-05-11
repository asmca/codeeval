import sys

from itertools import count



test_case=open(sys.argv[1],'r')
for test in test_case:
    mystr=filter(str.isalpha,test).lower()
    mydict={}
    for i in mystr:
        mydict[i]=0
    for i in mystr:
        mydict[i]+=1
    myarray=sorted(mydict.values(),reverse=True)
    
    if len(myarray)>26:
        print -1
        continue

    sum=0
    for i in count(26,-1):
        j=26-i;
        if j>=len(myarray):
            print sum
            break
        sum+=i*myarray[j]    

test_case.close()    
