import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    myinput=[int(x) for x in test.strip().split(' ')]
    
    number=myinput[0]
    myinput=myinput[1:]


    deltalist=[myinput[i+1]-myinput[i] for i in range(number-1) ]
    
    newdeltalist=[abs(x) for x in deltalist]
    sorted(newdeltalist)


    isJolly=1

    for i in range(len(newdeltalist)):
        if newdeltalist[i] != i+1:
            isJolly=0
            break


    print "Jolly" if isJolly else 'Not jolly'    


test_cases.close()



