import sys,string


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if not test.strip():
        continue
    string_list=list(string.lowercase)
    test_string=test.strip().lower()

    missing_list=[ x for x in string_list if x not in test_string ]

    print ''.join(missing_list) if not not missing_list else "NULL"
test_cases.close()



