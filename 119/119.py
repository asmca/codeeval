import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    # 
    # The addresses are integers in range [2, 10000] 
    # so we convert BEGIN -->0    END--> 1
    #
      #
    t=test.strip().replace('BEGIN','0').replace('END','1').split(';')

    s=[x.split('-') for x in t]

    GOOD=1 # default is a good chain
    for i in s:
        if i[0]==i[1]:
            GOOD=0
        break
    if not GOOD:
        print "BAD"
        continue

    s0=[i[0] for i in s]
    s1=[i[1] for i in s]
    if '0' not in s0 or '1' not in s1: # BEGIN/END not complete...
        print "BAD"
        continue
    idx=s0.index('0')
    # s2 is a tmp list, marking if path used..
    s2=[0 for x in range(len(s))] 

    for i in range(len(s)):
        if s2[idx]:
            GOOD=0
            break
        if s1[idx]=='1' and i+1!=len(s):
            GOOD=0
            break
        s2[idx]=1
        if i+1<len(s):
            idx=s0.index(s1[idx]) # recursive

    print "GOOD" if GOOD else "BAD"

test_case.close()    
