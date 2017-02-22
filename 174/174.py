import sys

slang_list = [
    ', yeah!',
    ', this is crazy, I tell ya.',
    ', can U believe this?',
    ', eh?',
    ', aw yea.',
    ', yo.',
    '? No way!',
    '. Awesome!',
]


new_str = ''
counter_1 = 0  # counter of 0/1 on punctuation mark
counter_2 = 0  # counter of slang_list index
with open(sys.argv[1], 'r') as test_cases:
    test_str = test_cases.read()
    for i in test_str:
        if i == '.' or i == '!' or i == '?':
            counter_1 ^= 1  # add counter 1
            if counter_1 == 0:  # even
                new_str += slang_list[counter_2]
                counter_2 = (counter_2 + 1) % 8
            else:
                new_str += i
        else:
            new_str += i
    print new_str