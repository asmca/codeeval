import sys

test_case = open(sys.argv[1],'r')

for test in test_case:
    tmplist=test.strip().split(';')
    s_center=tmplist[0].split(':')[1].strip(' ').strip(')').strip('(')
    x_center=float(s_center.split(',')[0])
    y_center=float(s_center.split(',')[1])

    radius=float(tmplist[1].split(':')[1].strip(' ').strip(')').strip('('))

    s_point=tmplist[2].split(':')[1].strip(' ').strip(')').strip('(')
    x_point=float(s_point.split(',')[0])
    y_point=float(s_point.split(',')[1])

    print "true" if pow((x_point-x_center),2)+pow((y_point-y_center),2)<=pow(radius,2) else "false"

test_case.close()    
