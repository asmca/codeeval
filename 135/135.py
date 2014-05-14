import sys


def markPath(n):
    nmap=[]
    for i in range(len(n)):
        for j in range(len(n)):
            if i!=j and n[i][-1]==n[j][0]:
                nmap.append((i,j))
    return nmap

def findpath(tt,ii):
    # function where destroy struct of t/i
    # convert to local object
    t=tt[:]
    i=ii[:]
    # we dont have extra checks here.. 
    # for we assume i in t
    if i not in t:
        return 0 # you shall not run into this block
    if len(t)==1:
        return 1 # only 1 path item, length is 2
    t.remove(i) # rest of the list, remove item i
    # A patch here, following reduce work doesnt solve the problem, we should pop the loop items.
    for j in t:
        if j[1]==i[0] or j[1]==i[1]:
            t.remove(j)
    return 1 + reduce(  max,  [   findpath(t,x) for x in t if x[0]==i[1]  and x[1]!=i[0]        ]      ,0 )



def findlongest(t):
    if not t:
        return None 
    allpath=[]
    for i in t: # each item to a path start with i
        #pathstartwithi=findpath(t,i)
        allpath.append(findpath(t,i))
    return allpath    



test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mylist=test.strip().split(',')

    t=markPath(mylist)

    w=findlongest(t)
    if not w: # result not empty
        print None
        continue
    print reduce(  max, w,0)+1

test_cases.close()

