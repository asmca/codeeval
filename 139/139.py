import sys

#init a dictionary for calendar
d_calendar={}
#for i in range(1990,2021):
#    d_calendar[i]=[0 for x in range(12)]

d_month={
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12,
        }
 

def work_record(cal,a,b):
    if b[0]==a[0]:
        for x in range(a[1],b[1]+1):
            cal[a[0]][x]=1
        return cal
    for x in range(a[1],12):
        cal[a[0]][x]=1
    for x in range(0,b[1]+1):
        cal[b[0]][x]=1
    if b[0]-a[0]>1:
        for y in range(a[0]+1,b[0]):
            cal[y]=[1 for x in range(12)]
    return cal





test_case = open(sys.argv[1],'r')

for test in test_case:
    for i in range(1990,2021):
        d_calendar[i]=[0 for x in range(12)]
    work_list=test.strip().split(';')
    for i in work_list:
        m_from=i.split('-')[0].strip().split(' ')
        m_to=i.split('-')[1].strip().split(' ')

        #tuning the arr list
        m_from.append(int(m_from[1]))
        m_from.append(d_month[m_from[0]]-1)
        m_to.append(int(m_to[1]))
        m_to.append(d_month[m_to[0]]-1)
        
        m_from=m_from[2:]
        m_to=m_to[2:]
 
        
        d_calendar=work_record(d_calendar,m_from, m_to)
        
    #print d_calendar 
    month_all=0
    for i in range(1990,2021):
        month_all=month_all+sum(d_calendar[i])
  
    print month_all/12
   
test_case.close()    
