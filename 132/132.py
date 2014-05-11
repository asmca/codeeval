import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    myarr=test.strip().split(',')
    mydict={}
    for i in myarr:
        mydict[i]=1 if i not in mydict else mydict[i]+1

    cnt_all=len(myarr)
    nu_max=max(mydict,key=mydict.get)
    cnt_max=mydict[nu_max]
    

    print nu_max if cnt_max>cnt_all/2 else "None"
    

test_case.close()    

