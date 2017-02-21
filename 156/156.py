import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        my_i = 0  # iterator letters only.
        for i, n in enumerate(test):
            if n.isalpha():
                if my_i % 2 == 0:
                    sys.stdout.write(n.upper())
                else:
                    sys.stdout.write(n.lower())
                my_i += 1
            else:
                sys.stdout.write(n)



