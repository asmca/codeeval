import sys

# we will setup the map first
myin=["rbc vjnmkf kd yxyqci na rbc zjkfoscdd ew rbc ujllmcp",
        "tc rbkso rbyr ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "de kr kd eoya kw aej icfkici re zjkr",]

myout=["the public is amazed by the quickness of the juggler",
        "we think that our language is impossible to understand",
        "so it is okay if you decided to quit",]

mydict={}

for i,n in enumerate(myin):
    for j in range(len(n)):
        if n[j] not in mydict:
            mydict[n[j]]=myout[i][j]

"""
we can see mydict contains 
keys exclude v / x
values exclue g /h

Tips from title that v-->g
so  x->h

reverse as we decode
"""


mydict['g']='v'
mydict['h']='x'




test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    t=[ mydict[x] for x in   list(test.strip())]
    print ''.join(t)
test_cases.close()
