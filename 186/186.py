import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    days_base, arr_base = test.split(';')

    days = int(days_base)
    arr = [ int(a) for a in  arr_base.split()]


    if len(arr) < days:
        print 0
        continue
    if len(arr) == days:
        print max(0, sum(days))
        continue
    else:
        arr_sum =[ sum(arr[i:i+days]) for i in range(len(arr)-days+1) ]
        print max(max(arr_sum),0)
        continue



test_cases.close()

