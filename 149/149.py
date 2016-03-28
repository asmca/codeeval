import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        arr = test.strip().split()

        mynum=''

        for i in range(0,len(arr),2):
            if arr[i]=='0':
                mynum = mynum + arr[i+1]
            if arr[i] =='00':
                mynum = mynum +  len(arr[i+1])*'1'

        print int(mynum,2)


