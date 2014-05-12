import sys
test_case = open(sys.argv[1],'r')
for test in test_case:
    num=int(test.strip().split(';')[0])
    sudokulist=[int(x) for x in test.strip().split(';')[1].split(',')]

    tag=1
    sqrtnum=int(pow(num,.5)+0.01)

    total=sum(x for x in range(1,num+1))

    for n in range(num):
        if sum(sudokulist[n+y*num] for y in range(num)) != total:
            tag=0
            break
        if sum(sudokulist[x+n*num] for x in range(num)) !=total:
            tag=0
            break
        #following code to cal small blocks
        xs=(n*sqrtnum)%num
        ys=(n/sqrtnum)*sqrtnum
        sums=0
        for x in range(xs,xs+sqrtnum):
            for y in range(ys,ys+sqrtnum):
                sums=sums+sudokulist[x+y*num]
        if sums!=total:
            tag=0
            break

    print True if tag else False 

test_case.close()    
