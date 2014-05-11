import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    tmplist=[]
    for i in list(test):
        if i.isalnum():
           tmplist.append(float(i)) #or float

    #for easy reading
    x1=tmplist[0] 
    y1=tmplist[1] 
    x2=tmplist[2] 
    y2=tmplist[3] 
    x3=tmplist[4] 
    y3=tmplist[5] 
    x4=tmplist[6] 
    y4=tmplist[7] 

    #get the position of center.
    #x,y
    #2(x2-x1)x + 2(y2-y1)y = x2**2 -x1**2 +y2**2-y1**2
    #2(x3-x2)x + 2(y3-y2)y = x3**2 -x2**2 +y3**2-y2**2
    a=2*(x2-x1)
    b=2*(y2-y1)
    c=pow(y2,2)+pow(x2,2)-pow(x1,2)-pow(y1,2)
    d=2*(x3-x2)
    e=2*(y3-y2)
    f=pow(y3,2)+pow(x3,2)-pow(x2,2)-pow(y2,2)
    
    if a==0 and d==0:
        print "false"
        continue
    if b*d==e*a:
        print "false"
        continue

    x=(b*f-e*c)/(b*d-e*a);
    y=(d*c-a*f)/(b*d-e*a);

    #we used point 1,2,3
    #here just checking point 4

    print "true " if abs(((x1-x)**2+(y1-y)**2)-((x4-x)**2+(y4-y)**2))<0.01 else "false"


test_case.close()    
