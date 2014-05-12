import sys

class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self,data,left=None,right=None ):
        """
        Node constructor
        @param data node data object
        """
        self.left = left
        self.right = right
        self.data = data
        self.para=None


def tag_para(a):
    for i in a.left, a.right:
        if not i:
            continue
        i.para=a
        tag_para(i)
        

def NodeSearch(a,x):
    if a.data==x:
        return a
    if a.left==None and a.right==None:
        return None
    return NodeSearch(a.left,x) or NodeSearch(a.right,x)

def WaytoRoot(x):
    Waylist=[x.data]
    i=x.para
    while i:
        Waylist.append(i.data)
        i=i.para
    Waylist.reverse()
    return Waylist


#init step to generate a tree
root=Node(data=30,left=Node(8,left=Node(3),right=Node(20,left=Node(10),right=Node(29))) ,right=Node(52)) 
tag_para(root)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    tmplist=test.strip().split(' ')
    x=NodeSearch(root,int(tmplist[0]))
    y=NodeSearch(root,int(tmplist[1]))

    listx=WaytoRoot(x)
    listy=WaytoRoot(y)

    mylen=len(listx) if len(listx)<=len(listy) else len(listy)

    for i in range(mylen):
        if listx[i] != listy[i]:
            print "None"
            break
        if i+1>=mylen or listx[i+1] != listy[i+1]:
            print listx[i]
            break

test_cases.close()



