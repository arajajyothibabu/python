__author__ = 'Araja Jyothi Babu'

def fibonacciSequence(limit):
    a = 0
    b = 1
    print a,
    print b,
    for i in range(limit):
        c = a  + b
        a = b
        b = c
        print c,

def test():
    fibonacciSequence(10)

test()
