import sys

test_case=open(sys.argv[1],'r')
for test in test_case:
    strn=test.strip()
    num=int(strn)
    if num<10:
        print True
        continue
    power=len(strn)
    sum=0
    for i in range(len(strn)):
        biti=int(strn[i])
        sum+=pow(biti,power)
    print True if sum==num else False

test_case.close()    
