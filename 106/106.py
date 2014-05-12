import sys

#I (capital i), V, X, L, C, D, and M 
mydict={
        1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M',
        4000:'Z',
        5000:'Z',
        9000:'Z',

        }



#c means 9, m means 100
# count, magnitude

def myrom(c,m):
    n=c*m
    if c==0:
        return ''
    if n>4000:
        return ''
    if n in mydict:
        return mydict[n]
    if c in range(2,4):
        return mydict[m]*c
    if c in range(6,9):
        return mydict[5*m]+myrom(c-5,m)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist=list(test.strip())
    myresult=[]
    for i in range(len(mylist)):
        m=pow(10,len(mylist)-1-i)
        c=int(mylist[i])
        myresult.append(myrom(c,m))
    print ''.join(myresult)    

test_cases.close()



