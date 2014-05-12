import sys

def push(a,m):
    a.append(m)

def pop(a):
    if not a:
        return None
    val=a[-1]
    a=a[:-1]
    return a,val

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist=[]
    myin=test.strip().split(' ')

    for i in myin:
        push(mylist,i)

    for i in range(len(mylist)):
        mylist,val=pop(mylist)
        if not i&1:
            print val,
    print
test_cases.close()



