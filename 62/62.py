import sys

def myMod(a,b):
    if a<0:
        return -1
    if a<b:
        return a;
    return a-a/b*b


test_case = open(sys.argv[1],'r')

for test in test_case:
    a,b=test.split(',')
    print myMod(int(a),int(b))

test_case.close()    


