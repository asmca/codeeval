from __future__ import division
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        my_expression = test.split()

        my_marks = my_expression[:len(my_expression)//2][::-1]
        my_numbers =[int(x) for x in my_expression[len(my_expression)//2:]]
        #print my_marks, my_numbers,

        my_result = my_numbers[0]
        for i, n in enumerate(my_marks):
            if n == '+':
                my_result += my_numbers[i+1]
            elif n == '*':
                my_result *= my_numbers[i+1]
            elif n == '/':
                my_result /= my_numbers[i+1]
        my_result = int(my_result + 0.5)
        print str(my_result)





