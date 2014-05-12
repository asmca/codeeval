import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    str1,str2=test.strip().split('|')
    newstr=''
    arr2=str2.strip().split(' ')
    for i in arr2:
        newstr+=str1[int(i)-1]
    print newstr    
test_case.close()    


