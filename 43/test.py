import math
n = 4
inp = [1,4,2,3]
out = []
for i in range(1,n):
        out.append(math.fabs(inp[i]-inp[i-1]))


out.sort()
val = 0

for i in range(1,n):
        print i,out[i-1]
        if out[i-1] == i:
                val = val+1


if val == n-1:
        print "jolly"
else:
        print "not jolly"



