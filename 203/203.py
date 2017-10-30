import sys

left_arrow = ">>-->"
right_arrow = "<--<<"


def count_arrow_string_line(string1, arrow):
    if string1.find(arrow) == -1:
        return 0
    myindex = string1.index(arrow) +4
    return 1 + count_arrow_string_line(string1[myindex:], arrow)


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    string_line = test.strip()
    print count_arrow_string_line(string_line, left_arrow) + count_arrow_string_line(string_line, right_arrow)


test_cases.close()
