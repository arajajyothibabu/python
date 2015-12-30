__author__ = 'Araja Jyothi Babu'

def isPrime(number):
    for i in range(2, number/2):
        if(number % 2 == 0):
            return False
    return True

def test():
    isPrime(5)
    isPrime(56)

test()