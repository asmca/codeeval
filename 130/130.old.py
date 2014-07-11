import sys,re

mylist={'0':"A+",
        '1':"(B+|A+)"
        }

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s1,s2=test.strip().split(' ')
    ss1=''.join([mylist[x] for x in s1 ])
    for i in range(len(ss1)):
        if i >=len(ss1)-1:
            break
      #  if ss1[i:i+8]=="+(B+|A+)" :
      #      ss1=ss1[:i+6]+ss1[i+7:]
      #  if ss1[i:i+4]=="+)A+":
      #      ss1=ss1[:i]+ss1[i+1:]
        if ss1[i:i+4]=="A+A+":
            ss1=ss1[:i+1]+ss1[i+2:]

    ss1='^'+ss1+'$'
    re1=re.compile(ss1)
    print "Yes" if re1.match(s2) else "No"


test_cases.close()
