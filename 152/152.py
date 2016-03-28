import sys

def f(x):
    if x<0 or x>100:
        return "This program is for humans"
    elif x<3:
        return "Still in Mama's arms"
    elif x<5:
        return  'Preschool Maniac'
    elif x<12:
        return   'Elementary school'
    elif x<15:
        return 'Middle school'
    elif x<19:
        return 'High school'
    elif x<23:
        return   'College'
    elif x<66:
        return 'Working for the man'
    elif x<101:
        return  'The Golden Years'


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print f(int(test.strip()))




