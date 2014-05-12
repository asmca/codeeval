import sys

def ifPair(a,b):
    s=a+b
    if s=='[]' or s=='{}' or s=='()':
        return True
    return False    


test_case = open(sys.argv[1],'r')

for test in test_case:
    mystr=test.strip()

    while 1:
        if not mystr:
            print True
            break
        tag=0
        for i in range(len(mystr)-1):    
            if ifPair(mystr[i],mystr[i+1]):
                mystr=mystr[:i]+mystr[i+2:]
                tag=1
                break
        if tag==0:
            print False
            break


test_case.close()


