__author__ = 'Araja Jyothi Babu'

def isLeapYear(year):
    if (year % 4 == 0 & year % 400 != 0 & year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def test():
    print isLeapYear(2012)
    print isLeapYear(1600)
    print isLeapYear(2017)

test()