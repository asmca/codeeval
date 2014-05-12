import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    myarray=test.strip().split(',')
    newarray=[]
    for i in range(len(myarray)):
        if myarray[i] in newarray:
            continue
        newarray.append(myarray[i])
    
    print ','.join(newarray)

test_case.close()    


