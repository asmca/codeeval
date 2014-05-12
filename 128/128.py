import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    myarr=test.strip().split(' ')
    compressedarr=[]
    for i in range(len(myarr)):
        if i==0:
            tarr=[myarr[i],1]
        elif myarr[i]==myarr[i-1]:
            tarr[1]+=1
        else:
            compressedarr.append(tarr)
            tarr=[myarr[i],1]
        if i+1==len(myarr):
            compressedarr.append(tarr)

    #print ' '.join(str(j[1])+' '+j[0] for j in compressedarr)

    for j in compressedarr:
        print j[1],j[0],
    print
test_case.close()


