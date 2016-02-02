__author__ = 'Araja Jyothi Babu'

def printPattern(rows = 3):
    for i in list(range(rows)) + list(reversed(range(rows-1))):
        print("{: <{w1}}{:$<{w2}}".format("", "", w1 = rows-i-1, w2 = 2*i+1))

def test():
    printPattern(5)

test()