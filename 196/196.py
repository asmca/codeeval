import sys


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        my_words = test.split()
        for my_word in my_words:
            print my_word[-1] + my_word[1:-1] + my_word[0],
        print ''
