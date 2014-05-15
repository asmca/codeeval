import sys

"""
Here we  Assume:
    1. hole is 2D
    2. bricks is 3D
    3. rectangular scenario.
    
To cross the hole:
    1. 2 sides of hole.
    2. 3 sides of brick
    3. 2 min sise of brick <= 2 sides of hole

"""

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    hole, bricks= test.split('|')

    # To get 2 sides of hole
    h=hole.split()
    h0=[ int(x) for x in   h[0].strip('[]').split(',')]
    h1=[ int (x) for x in  h[1].strip('[]').split(',')]
    s1=sorted([abs(h0[0]-h1[0]),abs(h0[1]-h1[1])   ])

    # To get 3 sides of brick(s).
    blist=bricks.strip().split(';')
    bnewlist=[]
    for i in blist:
        b=i.strip('()').split()
        b1=[ int(x) for x in   b[1].strip('[]').split(',')]
        b0=[ int(x) for x in   b[2].strip('[]').split(',')]
        bnewlist.append( [ int(b[0]), sorted([abs(b1[0]-b0[0]),abs(b1[1]-b0[1]),abs(b1[2]-b0[2])  ])]    )

    """
    bnewlist like:

    [      ['1', [2, 2, 8]]    ,             ['2', [2, 5, 7]]       ]

    """

    """
    To get the brick list can across the hole

    using list s1  and bnewlist
    """
    finallist=[]
    for i in bnewlist:
        if i[1][0]<=s1[0]  and i[1][1]<=s1[1]:
            finallist.append(i[0])

    if not finallist:
        print '-'
        continue
    finallist.sort()
    print ','.join( str(x) for x in   finallist)
    

test_cases.close()





    




