import sys, math

COL_SIZE=8
LINE_START = ord('a')
LINE_STOP = ord('h')

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        MY_LINE_NU = ord(test[0])
        MY_COL_NU = int(test[1])
        # MY_LIST = []
        # if MY_LINE_NU - 1 >= LINE_START:   # left > a
        #     POS_LEFT = chr(MY_LINE_NU - 1) + str(MY_COL_NU)
        #     MY_LIST.append(POS_LEFT)
        # if MY_LINE_NU + 1 <= LINE_STOP:    # right < h
        #     POS_RIGHT = chr(MY_LINE_NU + 1) + str(MY_COL_NU)
        #     MY_LIST.append(POS_RIGHT)
        # if MY_COL_NU - 1 >= 1:             # lower >1
        #     POS_LOWER = chr(MY_LINE_NU) + str(MY_COL_NU - 1)
        # if MY_COL_NU + 1 <= 8:             # upper <8
        #     POS_LOWER = chr(MY_LINE_NU) + str(MY_COL_NU + 1)
        MY_LIST = [
            [MY_LINE_NU - 2, MY_COL_NU - 1],
            [MY_LINE_NU - 2, MY_COL_NU + 1],
            [MY_LINE_NU + 2, MY_COL_NU - 1],
            [MY_LINE_NU + 2, MY_COL_NU + 1],
            [MY_LINE_NU + 1, MY_COL_NU - 2],
            [MY_LINE_NU + 1, MY_COL_NU + 2],
            [MY_LINE_NU - 1, MY_COL_NU - 2],
            [MY_LINE_NU - 1, MY_COL_NU + 2],
        ]
        stoke_list = []
        for i in MY_LIST:
            if LINE_START <= i[0] <= LINE_STOP and 1 <= i[1] <= 8:
                stoke_i = chr(i[0]) + str(i[1])
                stoke_list.append(stoke_i)
        stoke_list.sort()
        print ' '.join(stoke_list)