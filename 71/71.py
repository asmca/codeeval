import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    mylist=test.strip().split(';')[0].split(',')
    interval=int(test.strip().split(';')[1])

    newlist=[]
    for i in range(0,len(mylist),interval):
        if i+interval>len(mylist):
            newlist.extend(mylist[i:])
            break
        newlist.extend(mylist[i:i+interval][::-1])

    print ','.join(newlist)

test_case.close()    
