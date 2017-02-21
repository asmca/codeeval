import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        myangle = float(test)
        hr = int(myangle)

        myangle_min = (myangle - hr) * 60
        min = int(myangle_min)

        myangle_sec = (myangle_min - min) * 60
        sec = int(myangle_sec)

        sys.stdout.write(str(hr))
        sys.stdout.write('.')
        sys.stdout.write(str(min).zfill(2))
        sys.stdout.write('\'')
        sys.stdout.write(str(sec).zfill(2))
        sys.stdout.write('\"')

        print ''

