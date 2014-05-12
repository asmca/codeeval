import sys

test_case = open(sys.argv[1],'r')
for test in test_case:
    num1=int(test.strip().split(',')[0])
    num2=int(test.strip().split(',')[1])

    mylist=[x for x in range(num1)]

    index=num2-1
    step=num2
    
    while mylist:
        print mylist[index],
        mylist.remove(mylist[index])
        if not mylist:
            break
        index=(index-1+step)%len(mylist)
    print

test_case.close()    
