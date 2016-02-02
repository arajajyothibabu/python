__author__ = 'Araja Jyothi Babu'
import keyword

def wordInKeywords(word):
    return word in keyword.kwlist

def test():
    wordInKeywords("JB")

test()