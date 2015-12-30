__author__ = 'Araja Jyothi Babu'

def swap(x, y):
    return y, x

def test():
    swap(5, 6)
    assert 6, 5 == swap(5, 6)

test()