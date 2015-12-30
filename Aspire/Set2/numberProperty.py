__author__ = 'Araja Jyothi Babu'

def reverseOfNumber(number):
    sum  = 0
    while number > 0:
        sum = sum * 10 + number % 10
        number /= 10
    return sum

def isPalindrome(number):
    return number == reverseOfNumber(number)

def isPrime(number):
    for i in range(2, number/2):
        if(number % 2 == 0):
            return False
    return True

def isEven(number):
    return number % 2 == 0

def numberProperty(number):
    if isPalindrome(number):
        print "It's a Palindrome"
    if isPrime(number):
        print "It's a Prime"
    if isEven(number):
        print "It's an Even"

def test():
    numberProperty(5)
    numberProperty(111)
    numberProperty(56)

test()