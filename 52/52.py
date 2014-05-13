import sys


dvalue1={
        #'0':"zero",
        # here we format 0 to empty token, to save time...
        '0':"",
        '1':"One",
        '2':"Two",
        '3':"Three",
        '4':"Four",
        '5':"Five",
        '6':"Six",
        '7':"Seven",
        '8':"Eight",
        '9':"Nine",
        }

dvalue2={
        # Leave 0 1 as empty...
        # u share not run into 0 or 1
        '0':"",
        '1':"",
        '2':"Twenty",
        '3':"Thirty",
        '4':"Forty",
        '5':"Fifty",
        '6':"Sixty",
        '7':"Seventy",
        '8':"Eighty",
        '9':"Ninety",
        }

dvalue21={
        '10':"Ten",
        '11':"Eleven",
        '12':"Twelve",
        '13':"Thirteen",
        '14':"Fourteen",
        '15':"Fifteen",
        '16':"Sixteen",
        '17':"Seventeen",
        '18':"Eighteen",
        '19':"Nineteen",
        }


def toText(s):
    if not s:
        #print "You Should not run into this block!"
        return None
    n=len(s)
    if n==1:
        if s in dvalue1:
            return dvalue1[s]
        return None # this line is extra
    if n==2:
        if s[0]=='1':
            if s in dvalue21:
                return dvalue21[s]
        if s[0]=='0':
            return toText(s[1])
        # when n==2, s[0]>1
        # we searching dvalue2
        if s[0] in dvalue2:
            return dvalue2[s[0]]+toText(s[1])
        return None
    if n==3:
        if s[0]=='0':
            return toText(s[1:])
        if s[0] in dvalue1:
            return dvalue1[s[0]]+"Hundred"+toText(s[1:])
        return None
    if n>6:
        if int(s[:-6])==0:
            return  toText(s[-6:])
        return toText(s[:-6])+"Million"+toText(s[-6:])
    if n>3:
        if int(s[:-3])==0:
            return  toText(s[-3:])
        return toText(s[:-3])+"Thousand"+toText(s[-3:])
    # You should not run into this block!
    return None

        





test_case=open(sys.argv[1],'r')

for test in test_case:
    s=test.strip()
    """
    ASSUME: all plurals.
    if int(s)==0:
        print "ZeroDollar"
        continue
    if int(s)==1:
        print "OneDollar"
        continue
    """


    # here we guest test>1, so we use Dollar(s) here / plural
    print toText(s)+"Dollars"

test_case.close()    
