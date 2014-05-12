import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    mystr,mychr=test.strip().split(',')
    if mychr=='':
        print -1
        continue
    if mystr.find(mychr) == -1:
        print -1
        continue
    print len(mystr)-mystr[::-1].find(mychr)-1
            

test_case.close()    


