import sys



test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    myarr=test.strip().split(',')
    arr_nu=[]
    arr_aa=[]
    for i in myarr:
        if i.isdigit():
            arr_nu.append(i)
        elif i.isalpha():
            arr_aa.append(i)
    
    sep='' if not arr_nu or not arr_aa else '|'
    print ','.join(arr_aa)+sep+','.join(arr_nu)

test_cases.close()

