import sys
#
#
# def isPrime(n):
#     import math
#     if n == 1:
#         return False
#     elif n < 4:
#         return True
#     elif n & 1 == 0:
#         return False
#     elif n < 9:
#         return True
#     elif n % 3 == 0:
#         return False
#     else:
#         r = math.floor(math.sqrt(n))
#         f = 5
#         while f <= r:
#             if n % f == 0:
#                 return False
#             if n % (f + 2) == 0:
#                 return False
#             f += 6
#         return True
#
#
# def is2Squared(n):
#     if n < 1:
#         return False
#     elif (n+1) & n == 0:
#         return True
#     return False
#
# myset = set()
# for i in range(1, 30000):
#     if is2Squared(i) and isPrime(i):
#         myset.add(i)
# print str(myset)
#

myset = (31, 127, 3, 2047, 7)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    nu_input = int(test)
    nu_list = [str(i) for i in range(3, nu_input) if i in myset]
    print ', '.join(nu_list)

test_cases.close()
