import sys

def period(s):
    if not s:
        return 0
    j=len(s)  #j is the length of string
    if j==1:
        return 1
    for i in range(1,j+1): #i iterator
        if j%i:
            continue
        if i==j:
            return i
        b=True # a valid bit
        k=j/i       #k is the count of periods if true
        for i2 in range(k-1): #i2 2nd iterator
            if s[(i2*i):(i2*i+i)]!=s[(i2*i+i):(i2*i+i*2)]:
                b=False
                break
        if b:
            return i


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mystr=test.strip()
    print period(mystr)



test_cases.close()

