import sys

class Rectangle(object):
    """docstring for Rectangle"""
    def __init__(self, left,  up, right,low):
        self.left=left
        self.right=right
        self.up=up
        self.low=low
        self.size=(up-low)*(right-left)

#if a<b
def isNotOverlapping(a,b):
    return a.right<b.left or\
            a.left>b.right or\
            a.up<b.low or\
            a.low>b.up


test_case = open(sys.argv[1],'r')

for test in test_case:
    mylist=[int(x) for x in test.strip().split(',')]

    R_a=Rectangle(mylist[0],mylist[1],mylist[2],mylist[3])
    R_b=Rectangle(mylist[4],mylist[5],mylist[6],mylist[7])

    #  a is smaller than b
    if R_a.size<=R_b.size:
        a,b=R_a,R_b 
    else:
        a,b=R_b,R_a
    

    # check if vertex of a in b
    # size of a<b
    print not isNotOverlapping(a,b)

test_case.close()    

