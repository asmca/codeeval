import sys,operator

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist=test.strip().split(' ')
    mydict={}
    for i in mylist:
        mydict[mylist.index(i)]=[len(i),mylist.index(i),i] #sorted by index

    mylist2=mydict.values() #list to sort
    maxleng=max([x[0] for x in mylist2])

    minindex=min(x[1] for x in mylist2 if x[0]==maxleng)
        
#    minindex=len(mylist2)
#    for i in mylist2:
#        if i[0]==maxleng:
#            if i[1]<minindex:
#                minindex=i[1]
    for i in mylist2:
        if i[1]==minindex:
            print i[2]
    


test_cases.close()

