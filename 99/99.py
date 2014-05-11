import sys

def cal_dist(myarr):
    x1,y1=myarr[0].split(',')
    x2,y2=myarr[1].split(',')
    return pow((pow((int(x1)-int(x2)),2)+pow((int(y1)-int(y2)),2)),.5)

test_case = open(sys.argv[1],'r')

for test in test_case:
    myarr=test.replace('(','').strip(')').split(')')
    print int(cal_dist(myarr))

test_case.close()    


