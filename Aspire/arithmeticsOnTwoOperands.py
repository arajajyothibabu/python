__author__ = 'Araja Jyothi Babu'

def arithmeticsOnTwoOperands(x, y):
    print "Addition:", x + y
    print "Subtraction:", x - y
    print "Multiplication:", x * y
    print "Division:", x / y
    print "Floor Division:", x // y
    print "Exponentiation:", x ** y

def test():
    x = int(raw_input("Enter Operand-1"))
    y = int(raw_input("Enter Operand-1"))
    arithmeticsOnTwoOperands(x, y)

test()