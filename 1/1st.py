
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test_array=test.split(' ')
    test_nu_a=int(test_array[0])
    test_nu_b=int(test_array[1])
    test_nu_len=int(test_array[2])

    #new_array=[]
    for i in range(test_nu_len):
        j=i+1
        myitem=''

        if (j%test_nu_a)==0:
            myitem+='F'
        if (j%test_nu_b)==0:
            myitem+='B'
        if (j%test_nu_a) and (j%test_nu_b):
            myitem=j
        
        print myitem,
        #new_array.append(myitem)
    print 
    #print new_array

test_cases.close()
