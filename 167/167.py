import sys

str_read_more = '... <Read More>'

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        orig_str = test.rstrip()
        if len(orig_str) <= 55:  ## if the str length <=55
            print orig_str
            continue

        orig_str_40 = orig_str[:40]  ## if the str length >55
        space_idx = orig_str_40[::-1].find(' ')
        if space_idx == -1:
            final_str = orig_str_40 + str_read_more
        else:
            final_str = orig_str_40[:39 - space_idx] + str_read_more
        print final_str




