import sys
test_cases = open(sys.argv[1], 'r')
for strn in test_cases:
    for word in strn[::-1].split():
        print word[::-1],
    print

test_cases.close()

