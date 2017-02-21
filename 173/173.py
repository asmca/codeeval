import sys


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        my_new_str = ''  # new str.
        for n in test:
            if len(my_new_str) > 0 and n == my_new_str[-1]:
                pass  # do nothing
            else:
                my_new_str += n
        print my_new_str,


