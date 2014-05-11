import sys

mydict={
        'a':0,
        'b':1,
        'c':2,
        'd':3,
        'e':4,
        'f':5,
        'g':6,
        'h':7,
        'i':8,
        'j':9,
        'k':10,
        'l':11,
        'm':12,
        'n':13,
        'o':14,
        'p':15,
        'q':16,
        'r':17,
        's':18,
        't':19,
        'u':20,
        'v':21,
        'w':22,
        'x':23,
        'y':24,
        'z':25
        }

test_case = open(sys.argv[1],'r')

for test in test_case:
    str1=test.strip().split(' ')[0]
    str2=test.strip().split(' ')[1]

    newarr=[]
    for i in str2:
        if i in mydict:
            newarr.append(str1[mydict[i]])
        else:
            newarr.append(i)
    
    #print eval(''.join(newarr))

        for i in '+','-':
            if i in newarr:
                indexi=newarr.index(i)
                while 1:
                    if indexi+2>=len(newarr):
                        break
                    if newarr[indexi+1]!='0':
                        break
                    newarr.pop(indexi+1)

    print eval(''.join(newarr))

test_case.close()    


