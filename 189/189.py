import sys

def calc_distance(mylist, myitem):
    my_distance_list = map(lambda x: abs(x - myitem), mylist)
    return sum(my_distance_list)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        myarr=test.strip().split()
        if not myarr:
            continue
        num_friends = int(myarr[0])
        house_list = [int(i) for i in myarr[1:]]
        house_list.sort()
        if len(house_list) != num_friends:
            print "length failed"
            continue
        distance_list = [calc_distance(house_list, j) for j in house_list]
        print min(distance_list)




