import sys

mydict={
        '.-':'A',
        '-...':'B',
        '-.-.':'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.':'G',
        '....':'H',
        '..':'I',
        '.---':'J',
        '-.-':'K',
        '.-..':'L',
        '--':'M',
        '-.':'N',
        '---':'O',
        '.--.':'P',
        '--.-':'Q',
        '.-.':'R',
        '...':'S',
        '-':'T',
        '..-':'U',
        '...-':'V',
        '.--':'W',
        '-..-':'X',
        '-.--': 'Y',
        '--..' :'Z',
        '.----':'1',
        '..---':'2',
        '...--':'3',
        '....-':'4',
        '.....':'5',
        '-....':'6',
        '--...':'7',
        '---..':'8',
        '----.':'9',
        '-----':'0'
        }


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words=test.strip().split('  ')
    for i in words:
        codei=i.split(' ')
        mywords=[mydict[j] for j in codei]
        print ''.join(mywords),
    print
test_cases.close()

