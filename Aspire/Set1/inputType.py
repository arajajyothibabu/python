__author__ = 'Araja Jyothi Babu'

def testInputForamt(arg):
    if type(arg) is str:
        print "This is raw_input"
    else:
        print "This is just input"

def test():
    rawarg = raw_input("Enter raw input:")
    testInputForamt(rawarg)
    arg = input("Enter just input:")
    testInputForamt(arg)

test()