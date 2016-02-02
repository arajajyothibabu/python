__author__ = 'Araja Jyothi Babu'

def commonCharacters(str1, str2):
    print "Common Letters: "
    for ch in set(str1) & set(str2):
        print ch,

def test():
    commonCharacters("araja", "indraja")

test()