import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    mylist=test.strip().strip(';').split(';')
    kmlist=sorted([int(x.split(',')[1]) for x in mylist])
    
    deltalist=[kmlist[x]-kmlist[x-1] for x in range(len(kmlist)) if x>0 ]
    deltalist.insert(0,kmlist[0])
    print ','.join(str(v) for v in deltalist)
    
test_case.close()    


