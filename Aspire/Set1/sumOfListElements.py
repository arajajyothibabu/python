__author__ = 'Araja Jyothi Babu'

def sumOfListElements(list):
    return sum(list)

def test():
    print sumOfListElements([1,2,3,4,5])
    print sumOfListElements(list(range(20)))

test()