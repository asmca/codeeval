import sys

def myupper(s):
    return s[0].upper()+s[1:]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    myarr=test.split(' ')
    print ' '.join([myupper(i) for i in myarr]),
    
    


test_cases.close()

