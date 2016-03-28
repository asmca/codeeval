import sys


line =[
'-**----*--***--***---*---****--**--****--**---**--',
'*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-',
'*--*---*---**---**--****-***--***----*---**---***-',
'*--*---*--*-------*----*----*-*--*--*---*--*----*-',
'-**---***-****-***-----*-***---**---*----**---**--',
'--------------------------------------------------',
]

with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            test_nu = filter(str.isdigit, test)
            for i in range(6):
                for item in test_nu:
                    j = int(item)
                    sys.stdout.softspace=False; print line[i][5*j:5*j+5],
                print


