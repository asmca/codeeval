import sys

a=[[0 for x in range(256)] for y in range(256)]


def setRow(i,x):
    for j in range(256):
        a[i][j]=x

def setCol(j,x):
    for i in range(256):
        a[i][j]=x

def queryRow(i):
    sum=0
    for j in range(256):
        sum+=a[i][j]
    print sum    

def queryCol(j):
    sum=0
    for i in range(256):
        sum+=a[i][j]
    print sum    


mydict={
    'SetRow': setRow,
    "SetCol": setCol,
    "QueryRow": queryRow,
    "QueryCol": queryCol,
    }

test_case = open(sys.argv[1],'r')

for test in test_case:
    testarray=test.split(' ')
    mycmd=testarray[0]
    my1st=int(testarray[1])

    
    if mycmd in mydict:
        if len(testarray)==3:
            my2nd=int(testarray[2])
            mydict[mycmd](my1st,my2nd)
        elif len(testarray)==2:
            mydict[mycmd](my1st)

test_case.close()    


