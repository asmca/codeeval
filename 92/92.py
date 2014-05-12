import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
   myarray=test.strip().split(' ')
   print myarray[-2] if len(myarray)>=2 else ''

test_case.close()    


