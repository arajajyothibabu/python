__author__ = 'Araja Jyothi Babu'

def largestOfThree(x, y, z):
    return x if (x > y and x > z) else y if y > z else z

def test():
    print largestOfThree(1,2,3)
    print largestOfThree(2,3,1)
    print largestOfThree(3,2,1)

test()