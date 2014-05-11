import sys

L_reg=[100.00,50.00,20.00,10.00,5.00,2.00,1.00,.50,.25,.10,.05,.01]

D_reg={
        100.00:'ONE HUNDRED',
        50.00:'FIFTY',
        20.00:'TWENTY',
        10.00:'TEN',
        5.00:'FIVE',
        2.00:'TWO',
        1.00:'ONE',
        .50:'HALF DOLLAR',
        .25:'QUARTER',
        .10:'DIME',
        .05:'NICKEL',
        .01:'PENNY',
        }

test_case = open(sys.argv[1],'r')

for test in test_case:
    myarray=test.strip().split(';')
    ch=float(myarray[1])
    pp=float(myarray[0])

    if ch<pp:
        print "ERROR"
        continue
    if ch==pp:
        print "ZERO"
        continue

    rest=ch-pp

    

    L_rest=[]
    while 1:
        if rest<0.002:
            break
        for i in L_reg:
            if rest+0.001>=i:
                rest=rest-i
                L_rest.append(D_reg[i])
                break

    print ','.join(L_rest)
                            


test_case.close()    


