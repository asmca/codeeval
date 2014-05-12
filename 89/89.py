import sys

mlist=[]
test_case = open(sys.argv[1],'r')
for test in test_case:
    if not not test.strip():
        mlist.append([int(x) for x in test.strip().split(' ')])
test_case.close()    

max_sum_before=[]
for i in range(len(mlist)-1,0-1,-1):
    if max_sum_before:
        max_sum_next=[0 for x in range(i+1)]
        for x in range(i+1):
            max_sum_next[x]=mlist[i][x]+max(max_sum_before[x],max_sum_before[x+1])
        max_sum_before=max_sum_next
    else:    
        max_sum_before=mlist[i]

print max_sum_before[0]
