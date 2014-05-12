import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    myarray=test.strip().split(';')
    myarr1=myarray[0].split(',')
    myarr2=myarray[1].split(',')

    tparr=[]
    for i in myarr1:
        if i in myarr2:
            tparr.append(i)
            
    print ','.join(tparr)

test_case.close()    


