import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    myarr=[]
    for i in test:
        if i.islower():
            myarr.append(i.upper())
            continue
        myarr.append(i.lower())

    print ''.join(myarr),

test_case.close()    


