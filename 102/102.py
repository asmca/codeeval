import sys,json


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    mydict=json.loads(test) 
    myitems=mydict.get("menu").get("items")    
    sum=0
    for i in range(len(myitems)):
        if myitems[i] is None:
            continue
        if "label" in myitems[i]:
            sum+=myitems[i]["id"]
    print sum

test_cases.close()

