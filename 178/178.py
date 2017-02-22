import sys,math


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        my_matrix = test.split()
        my_len = len(my_matrix)  # line size of each side.
        final_matrix = ['*'] * my_len
        m = 0  # line
        column_size = int(math.sqrt(my_len) + 0.5)   # column size
        n = column_size - 1

        for i, j in enumerate(my_matrix):
            final_matrix[m * column_size + n] = j
            m += 1
            if m >= column_size:
                m %= column_size
                n -= 1
        print ' '.join(final_matrix)





