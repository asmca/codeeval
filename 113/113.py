import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    arr1=test.split('|')[0].strip().split(' ')
    arr2=test.split('|')[1].strip().split(' ')
    arr3=[int(arr1[i])*int(arr2[i]) for i in range(len(arr1)) ]

    print ' '.join(str(v) for v in arr3)

test_cases.close()

