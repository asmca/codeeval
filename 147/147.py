import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        myindex=sorted(test.strip()+'a').index('a')
        upper_no = myindex
        #lower_no = len(test)- myindex

        total_no = float(len(test.strip()))

        lower_perc = '{:.2f}'.format(round(100*(total_no - upper_no)/total_no,2))
        upper_perc = '{:.2f}'.format(round(100*(upper_no)/total_no,2))

        print "lowercase:", lower_perc , "uppercase:", upper_perc

