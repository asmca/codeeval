import sys,codecs

def myprocess(s):
    for i in range(len(s)):
        if i+1>=len(s):
            break
        if s[i]=='%':
            try:
                int(s[i+1:i+3],16)
                sdecode=s[i+1:i+3].decode('hex')
                s=s[:i]+sdecode+s[i+3:]
            except ValueError:
                i
    while ':80' in s:
        i=s.index(':80')
        s=s[:i]+s[i+3:]
    return s.lower()

test_case = open(sys.argv[1],'r')

for test in test_case:
    s1=test.strip().split(';')[0]
    s2=test.strip().split(';')[1]
    
    ss1=myprocess(s1)
    ss2=myprocess(s2)

    print True if ss1==ss2 else False

test_case.close()    
