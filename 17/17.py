import sys

def max_sub(A):
    max_ending_here=max_so_far=A[0]
    for i in A[1:]:
        max_ending_here=max(i,max_ending_here+i)
        max_so_far=max(max_so_far,max_ending_here)
    return max_so_far

test_case=open(sys.argv[1],'r')
for test in test_case:
    mylist=[int(a) for a in test.split(',')]
    print max_sub(mylist)

test_case.close()    
