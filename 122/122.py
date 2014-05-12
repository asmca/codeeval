import sys

mydict={
        'a':'0',
        'b':'1',
        'c':'2',
        'd':'3',
        'e':'4',
        'f':'5',
        'g':'6',
        'h':'7',
        'i':'8',
        'j':'9',
        '0':'0',
        '1':'1',
        '2':'2',
        '3':'3',
        '4':'4',
        '5':'5',
        '6':'6',
        '7':'7',
        '8':'8',
        '9':'9'
        }


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist=[mydict[i] for i in test if i in mydict]    
    if not mylist:
        print "NONE"
        continue
    print ''.join(mylist)

test_cases.close()
