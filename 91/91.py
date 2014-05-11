import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    strarr=test.strip().split(' ')
    if len(strarr)<1:
        print strarr,
        continue
    if len(strarr)==1:
        print strarr[0],
        continue
    mydict={}
    for i in range(len(strarr)):
        mydict[strarr[i]]=float(strarr[i])

    for w in sorted(mydict, key=mydict.get):
        print w,
    print

test_case.close()    


